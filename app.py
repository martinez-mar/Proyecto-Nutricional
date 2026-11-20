"""Aplicación de demostración: Analizador de Composición Nutricional.

Este cascarón utiliza datos de ejemplo en memoria. No almacena información
permanente ni sustituye una fuente profesional de orientación nutricional.
"""
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.config["SECRET_KEY"] = "cambia-esta-clave-en-produccion"

# Datos ilustrativos para la exposición. En la siguiente etapa se migrarán a SQLite.
CATEGORIES = [
    {"id": 1, "name": "Frutas", "description": "Frutas frescas y sus derivados"},
    {"id": 2, "name": "Verduras", "description": "Vegetales y hortalizas"},
    {"id": 3, "name": "Proteínas", "description": "Alimentos ricos en proteína"},
    {"id": 4, "name": "Cereales", "description": "Granos y derivados"},
    {"id": 5, "name": "Lácteos", "description": "Leche y productos lácteos"},
]

FOODS = [
    {"id": 1, "name": "Aguacate", "category_id": 1, "description": "Fruto con grasas principalmente monoinsaturadas.", "portion": "100 g",
     "nutrients": {"Calorías": 160, "Proteínas": 2.0, "Carbohidratos": 8.5, "Grasas": 14.7, "Fibra": 6.7}},
    {"id": 2, "name": "Plátano", "category_id": 1, "description": "Fruta fuente de carbohidratos y potasio.", "portion": "100 g",
     "nutrients": {"Calorías": 89, "Proteínas": 1.1, "Carbohidratos": 22.8, "Grasas": 0.3, "Fibra": 2.6}},
    {"id": 3, "name": "Espinaca", "category_id": 2, "description": "Vegetal de hoja verde con micronutrientes.", "portion": "100 g",
     "nutrients": {"Calorías": 23, "Proteínas": 2.9, "Carbohidratos": 3.6, "Grasas": 0.4, "Fibra": 2.2}},
    {"id": 4, "name": "Pechuga de pollo", "category_id": 3, "description": "Corte magro de pollo, sin piel.", "portion": "100 g",
     "nutrients": {"Calorías": 165, "Proteínas": 31.0, "Carbohidratos": 0.0, "Grasas": 3.6, "Fibra": 0.0}},
    {"id": 5, "name": "Avena", "category_id": 4, "description": "Cereal integral que aporta fibra.", "portion": "100 g",
     "nutrients": {"Calorías": 389, "Proteínas": 16.9, "Carbohidratos": 66.3, "Grasas": 6.9, "Fibra": 10.6}},
    {"id": 6, "name": "Yogur natural", "category_id": 5, "description": "Lácteo fermentado sin azúcar añadida en esta referencia.", "portion": "100 g",
     "nutrients": {"Calorías": 61, "Proteínas": 3.5, "Carbohidratos": 4.7, "Grasas": 3.3, "Fibra": 0.0}},
]

VITAMINS = [
    {"name": "Vitamina A", "function": "Participa en la visión, el crecimiento y el funcionamiento del sistema inmunitario.", "sources": "Zanahoria, camote, espinaca y huevo."},
    {"name": "Vitamina B12", "function": "Contribuye a la formación de glóbulos rojos y al funcionamiento del sistema nervioso.", "sources": "Pescado, carne, huevo y lácteos."},
    {"name": "Vitamina C", "function": "Participa en la formación de colágeno y favorece la absorción del hierro.", "sources": "Guayaba, cítricos, kiwi y pimiento."},
    {"name": "Vitamina D", "function": "Ayuda al aprovechamiento del calcio y al mantenimiento de los huesos.", "sources": "Pescados grasos, huevo y alimentos fortificados."},
    {"name": "Vitamina E", "function": "Actúa como antioxidante y ayuda a proteger las células.", "sources": "Semillas, nueces y aceites vegetales."},
    {"name": "Vitamina K", "function": "Interviene en la coagulación sanguínea y en la salud ósea.", "sources": "Verduras de hoja verde como espinaca y kale."},
]

def get_food(food_id):
    return next((food for food in FOODS if food["id"] == food_id), None)

def category_name(category_id):
    category = next((item for item in CATEGORIES if item["id"] == category_id), None)
    return category["name"] if category else "Sin categoría"

@app.context_processor
def inject_layout_data():
    return {"categories": CATEGORIES, "category_name": category_name}

@app.route("/")
def dashboard():
    recent_ids = session.get("history", [])[:4]
    recent_foods = [get_food(item["food_id"]) for item in recent_ids]
    return render_template("dashboard.html", page="inicio", foods=FOODS,
                           recent_foods=[food for food in recent_foods if food])

@app.route("/catalogo")
def catalog():
    search = request.args.get("q", "").strip().lower()
    category = request.args.get("categoria", "")
    foods = FOODS
    if search:
        foods = [food for food in foods if search in food["name"].lower()]
    if category.isdigit():
        foods = [food for food in foods if food["category_id"] == int(category)]
    return render_template("catalogo.html", page="catalogo", foods=foods,
                           search=request.args.get("q", ""), selected_category=category)

@app.route("/alimento/<int:food_id>")
def food_detail(food_id):
    food = get_food(food_id)
    if not food:
        flash("No se encontró el alimento solicitado.", "warning")
        return redirect(url_for("catalog"))
    history = session.get("history", [])
    history = [item for item in history if item["food_id"] != food_id]
    history.insert(0, {"food_id": food_id, "date": datetime.now().strftime("%d/%m/%Y %H:%M")})
    session["history"] = history[:20]
    return render_template("alimento.html", page="catalogo", food=food)

@app.route("/comparador", methods=["GET", "POST"])
def comparator():
    selected = request.form.getlist("food_ids") if request.method == "POST" else request.args.getlist("food_ids")
    selected_ids = {int(value) for value in selected if value.isdigit()}
    selected_foods = [food for food in FOODS if food["id"] in selected_ids]
    return render_template("comparador.html", page="comparador", foods=FOODS,
                           selected_foods=selected_foods)

@app.route("/vitaminas")
def vitamins():
    return render_template("vitaminas.html", page="vitaminas", vitamins=VITAMINS)

@app.route("/componentes")
def components():
    nutrient_names = sorted({name for food in FOODS for name in food["nutrients"]})
    return render_template("componentes.html", page="componentes",
                           nutrient_names=nutrient_names, foods=FOODS)

@app.route("/historial")
def history():
    entries = session.get("history", [])
    records = [{"food": get_food(item["food_id"]), "date": item["date"]} for item in entries]
    return render_template("historial.html", page="historial",
                           records=[record for record in records if record["food"]])

@app.errorhandler(404)
def not_found(_error):
    return render_template("404.html", page=""), 404

if __name__ == "__main__":
    app.run(debug=True)
