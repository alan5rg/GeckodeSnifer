#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#!UTC/Encode by Python with Monkey Python Coding Circus
#!Alan.R.G.Systemas & NOva DulceKali vibes

"""
GeckodeSnifer™ 4.1 PyQt5
Minimalista, Geckoniano y listo para generar informes supremos de proyectos Python
Sniffer estructural + interfaz profesional.
"""

# Roadmap: 

"""
🦎✨ GECKODESNIFER™ v4.0 — Team Cangurera Architecture Tool
-----------------------------------------------------------

GeckodeSnifer es una herramienta interna del Team Cangurera diseñada para
analizar, visualizar y mejorar proyectos Python de forma rápida y coherente
con el enfoque de desarrollo "Geckonismo Minimalista".

Su objetivo es ofrecer una visión clara del estado estructural del proyecto,
permitiendo detectar problemas de arquitectura, dependencias, complejidad y
documentación antes de que escalen.

En pocas palabras:
Snifiar el proyecto → Ver el mapa → Mejorar con criterio.


-----------------------------------------------------------
🦎 FUNCIONALIDADES ACTUALES (v4.1)
-----------------------------------------------------------

✔ Warm Up & AutoCheck
    El propio GeckodeSnifer se analiza a sí mismo al iniciar,
    generando un informe base de referencia.

✔ Project Sniffing
    Escaneo de archivos o directorios Python completos.

✔ Project Tree
    Visualización estructural del proyecto analizado.

✔ PAM — Project Architecture Map
    Mapa general de la arquitectura del proyecto.

✔ Gecko Audit
    Auditoría básica del código:
        - líneas por archivo
        - funciones detectadas
        - clases detectadas
        - posibles archivos grandes

✔ Gecko DepCheck
    Detección de imports y dependencias internas del proyecto.

✔ Gecko Recommendations
    Generación automática de sugerencias simples:
        - archivos demasiado largos
        - posibles refactors
        - mejoras de organización

✔ DocScore
    Estimación simple de calidad de documentación del proyecto
    basada en presencia de docstrings.

✔ Report Generator
    Generación de informes de análisis del proyecto.


-----------------------------------------------------------
🦎 GECKOPENDIENTES (IDEAS EN EXPLORACIÓN)
-----------------------------------------------------------

◇ Geckonstelación de Herencias
    Visualización del árbol de herencias entre clases del proyecto.

◇ Gecko Visual Architecture Graph
    Grafo visual de dependencias entre módulos y componentes.

◇ Complejidad Geckónica
    Métricas simples de complejidad por archivo o función.

◇ Detector de "Clases Monstruo"
    Identificación automática de clases con demasiadas responsabilidades.

◇ Dependency Heatmap
    Mapa de dependencias más utilizadas o más críticas.

◇ Arquitectura Evolutiva
    Comparación entre versiones del proyecto para ver
    cómo cambia la estructura con el tiempo.

◇ Gecko Refactor Hints
    Sugerencias automáticas de posibles refactors.

◇ Exportadores Avanzados
    Exportar análisis a:
        - Markdown
        - HTML
        - Diagramas

-----------------------------------------------------------
🦎 FILOSOFÍA DEL PROYECTO
-----------------------------------------------------------

GeckodeSnifer no busca ser una herramienta pesada ni intrusiva.

Su objetivo es simple:

    Ver claro.
    Detectar temprano.
    Construir mejor.

Un mapa claro del terreno permite construir software
más sólido, coherente y escalable.

Estilo de desarrollo:
🦎 Geckonismo Minimalista
✨ Claridad antes que complejidad
🚀 Arquitectura visible desde el inicio

-----------------------------------------------------------
Team Cangurera
"""

import os
import ast
import datetime
import sys

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QFileDialog,
    QTextEdit, QVBoxLayout, QPushButton,
    QTabWidget, QToolBar, QAction, QLabel, QSizePolicy
)

from PyQt5 import QtGui

from PyQt5.QtCore import QTimer, Qt, QSize

# Minimal MIT THeme
import qdarkstyle
from qdarkstyle import DarkPalette

# ---------------------------
# CORE ENGINE
# ---------------------------
class GeckodeSnifer:
    def __init__(self, project_path):
        self.project_path = project_path
        self.report = []

        self.files = 0
        self.classes = 0
        self.functions = 0
        self.docstrings = 0
        self.missing_docs = 0

        self.large_files = 0
        self.missing_deps = 0

        self.warmup_report = ""

    def sniff_project(self):

        self.report.append("🦎 GECKODE SNIFFER REPORT\n")
        self.report.append(f"Proyecto: {self.project_path}\n")

        self.evaluate_structure()

        for root, dirs, files in os.walk(self.project_path):
            for file in files:
                if file.endswith(".py"):

                    self.files += 1

                    full_path = os.path.join(root, file)
                    self.sniff_file(full_path)

        self.add_metrics()
        self.add_gecko_footprint()

        return "\n".join(self.report)

    def evaluate_structure(self):

        self.report.append("\n📁 Evaluación de estructura\n")

        if "main.py" in os.listdir(self.project_path):
            self.report.append("✔ main.py encontrado\n")
        else:
            self.report.append("⚠ No se encontró main.py\n")

    def sniff_file(self, filepath):

        self.report.append("\n" + "="*60)
        self.report.append(f"\nArchivo: {filepath}\n")

        try:

            with open(filepath, "r", encoding="utf-8") as f:
                source = f.read()

            tree = ast.parse(source)

            module_doc = ast.get_docstring(tree)

            if module_doc:
                self.docstrings += 1
                self.report.append("\n📜 Docstring del módulo:\n")
                self.report.append(module_doc + "\n")
            else:
                self.missing_docs += 1
                self.report.append("⚠ Módulo sin docstring\n")

            for node in ast.walk(tree):

                if isinstance(node, ast.ClassDef):

                    self.classes += 1
                    self.report.append(f"\n🏛 Clase: {node.name}")

                    doc = ast.get_docstring(node)

                    if doc:
                        self.docstrings += 1
                        self.report.append("Docstring de clase:")
                        self.report.append(doc)
                    else:
                        self.missing_docs += 1
                        self.report.append("⚠ Clase sin docstring")

                if isinstance(node, ast.FunctionDef):

                    self.functions += 1
                    self.report.append(f"\n⚙ Función: {node.name}")

                    doc = ast.get_docstring(node)

                    if doc:
                        self.docstrings += 1
                        self.report.append("Docstring de función:")
                        self.report.append(doc)
                    else:
                        self.missing_docs += 1
                        self.report.append("⚠ Función sin docstring")

        except Exception as e:
            self.report.append(f"❌ Error leyendo archivo: {e}")

    def add_metrics(self):

        total = self.docstrings + self.missing_docs

        if total == 0:
            score = 0
        else:
            score = int((self.docstrings / total) * 100)

        bar = "█" * (score // 10) + "░" * (10 - score // 10)

        self.report.append("\n\n📊 Gecko Documentation Metrics\n")

        self.report.append(f"Archivos Python analizados: {self.files}")
        self.report.append(f"Clases detectadas: {self.classes}")
        self.report.append(f"Funciones detectadas: {self.functions}")

        self.report.append(f"\nDocstrings encontrados: {self.docstrings}")
        self.report.append(f"Docstrings faltantes: {self.missing_docs}")

        self.report.append("\nGECKO DOC SCORE")
        self.report.append(f"{bar} {score}%")

        self.score = score

    def add_gecko_footprint(self):

        now = datetime.datetime.utcnow()

        self.report.append("\n\n🦎 Gecko Footprint")
        self.report.append("- Autor: Alan.R.G.Systemas & NOva DulceKali")
        self.report.append("- Tool: GeckodeSnifer™ 4.0 Deluxe")
        self.report.append("- Timestamp UTC: " + str(now))
        self.report.append("- Vibes: GeckoPrint Pythonista")

        self.warmup_report = (
            """
            \n\n🦎 Gecko Footprint:
            GeckodeSnifer™ 4.0 Deluxe
            Auto-Diagnostic Engine
            """
            + self.warmup_report
        )

    def audit_project(self):

        audit = []
        audit.append("🦎 GECKO AUDIT REPORT\n")

        self.large_files = 0
        long_functions = 0

        modules = {}
        imported_modules = set()

        for root, dirs, files in os.walk(self.project_path):

            for file in files:

                if file.endswith(".py"):

                    path = os.path.join(root, file)
                    module = os.path.splitext(file)[0]

                    modules[module] = path

                    with open(path, "r", encoding="utf-8") as f:
                        source = f.read()

                    lines = source.splitlines()

                    # 📦 archivo grande
                    if len(lines) > 500:
                        audit.append(f"⚠ Archivo grande detectado: {file} — {len(lines)} líneas")
                        audit.append("   Recomendación: dividir módulo")
                        self.large_files += 1

                    try:

                        tree = ast.parse(source)

                        functions = []
                        classes = []

                        imports = []
                        used_names = set()

                        for node in ast.walk(tree):

                            if isinstance(node, ast.FunctionDef):

                                functions.append(node.name)

                                if hasattr(node, "end_lineno"):

                                    length = node.end_lineno - node.lineno

                                    if length > 50:
                                        audit.append(
                                            f"⚠ Función extensa detectada: {node.name}() — {length} líneas"
                                        )
                                        long_functions += 1

                            if isinstance(node, ast.ClassDef):
                                classes.append(node.name)

                            if isinstance(node, ast.Import):

                                for n in node.names:
                                    imports.append(n.name.split(".")[0])
                                    imported_modules.add(n.name.split(".")[0])

                            if isinstance(node, ast.ImportFrom):

                                if node.module:
                                    imports.append(node.module.split(".")[0])
                                    imported_modules.add(node.module.split(".")[0])

                            if isinstance(node, ast.Name):
                                used_names.add(node.id)

                        # 📥 imports no usados
                        for imp in imports:

                            if imp not in used_names:
                                audit.append(f"⚠ Import posiblemente no utilizado: {imp}")

                        # 📁 módulos vacíos
                        if not functions and not classes:
                            audit.append(f"⚠ Archivo sin clases ni funciones: {file}")

                    except:
                        audit.append(f"⚠ Error analizando AST: {file}")

        # 🧬 módulos huérfanos
        for mod in modules:

            if mod not in imported_modules and mod != "main":
                audit.append(f"⚠ Módulo huérfano detectado: {mod}.py")

        audit.append(f"\nFunciones largas detectadas: {long_functions}")

        return "\n".join(audit)

    def check_dependencies(self):

        deps = set()

        for root, dirs, files in os.walk(self.project_path):

            for file in files:

                if file.endswith(".py"):

                    with open(os.path.join(root, file), "r", encoding="utf-8") as f:

                        tree = ast.parse(f.read())

                        for node in ast.walk(tree):

                            if isinstance(node, ast.Import):
                                for n in node.names:
                                    deps.add(n.name.split(".")[0])

                            if isinstance(node, ast.ImportFrom):
                                if node.module:
                                    deps.add(node.module.split(".")[0])

        report = []
        report.append("🦎 GECKO DEPENDENCY CHECK\n")

        missing = []

        for dep in sorted(deps):

            try:
                __import__(dep)
                report.append(f"{dep} ✔")
            except:
                report.append(f"{dep} ❌")
                missing.append(dep)

        report.append(f"\nDependencias faltantes: {len(missing)}")

        return "\n".join(report), len(missing)

    def generate_recommendations(self):

        rec = []

        rec.append("🦎 Gecko Recommendations\n")

        if self.missing_docs > 0:
            rec.append("• Mejorar documentación de funciones y clases")

        if self.large_files > 0:
            rec.append("• Dividir módulos demasiado grandes")

        if self.missing_deps > 0:
            rec.append("• Instalar dependencias faltantes")

        if not rec:
            rec.append("✔ Proyecto bien estructurado")

        return "\n".join(rec)

    # Refactorizacion de Metodo by Ei2 para mayor impacto visual con el uso de caracteres UNicode
    def build_project_tree(self):
        """
        Genera un árbol visual del proyecto con conectores dinámicos.
        """
        tree = []
        tree.append("🦎 GECKO PROJECT TREE\n")
        tree.append(f"Proyecto: {self.project_path}\n")

        base_path = os.path.abspath(self.project_path)
        
        def walk_level(directory, prefix=""):
            # Listamos y ordenamos: carpetas primero, luego archivos
            items = sorted(os.listdir(directory), key=lambda x: (not os.path.isdir(os.path.join(directory, x)), x.lower()))
            
            for i, item in enumerate(items):
                path = os.path.join(directory, item)
                is_last = (i == len(items) - 1)
                
                # Decidimos el conector de la rama actual
                connector = "└── " if is_last else "├── "
                tree.append(f"{prefix}{connector}{item}")
                
                # Si es un directorio, bajamos de nivel (recursión)
                if os.path.isdir(path):
                    # Si es el último, el prefijo para los hijos queda vacío, 
                    # si no, dibujamos la línea vertical de continuación
                    extension = "    " if is_last else "│   "
                    walk_level(path, prefix + extension)

        # Iniciamos el proceso desde la raíz
        root_name = os.path.basename(base_path) or base_path
        tree.append(root_name)
        walk_level(base_path)

        return "\n".join(tree)

    def build_architecture_map(self):
        """
        🦎 PAM — Project Architecture Map
        Detecta dependencias internas entre módulos.
        """

        modules = {}
        imports_map = {}

        for root, dirs, files in os.walk(self.project_path):

            for file in files:

                if file.endswith(".py"):

                    path = os.path.join(root, file)
                    module = os.path.splitext(file)[0]

                    modules[module] = path
                    imports_map[module] = []

                    try:

                        with open(path, "r", encoding="utf-8") as f:
                            tree = ast.parse(f.read())

                        for node in ast.walk(tree):

                            if isinstance(node, ast.Import):
                                for n in node.names:
                                    imports_map[module].append(n.name.split(".")[0])

                            if isinstance(node, ast.ImportFrom):
                                if node.module:
                                    imports_map[module].append(node.module.split(".")[0])

                    except:
                        pass

        report = []
        report.append("🦎 PROJECT ARCHITECTURE MAP\n")

        for mod in sorted(imports_map):

            report.append(f"\n📦 {mod}")

            for dep in imports_map[mod]:

                if dep in modules:
                    report.append(f"   └── {dep}")

        return "\n".join(report)

    def build_inheritance_constellation(self):

        classes = {}
        parents = {}

        for root, dirs, files in os.walk(self.project_path):
            for file in files:
                if file.endswith(".py"):
                    path = os.path.join(root, file)

                    try:
                        with open(path, "r", encoding="utf-8") as f:
                            tree = ast.parse(f.read())

                        for node in ast.walk(tree):
                            if isinstance(node, ast.ClassDef):
                                name = node.name
                                bases = []
                                for base in node.bases:
                                    if isinstance(base, ast.Name):
                                        bases.append(base.id)
                                    elif isinstance(base, ast.Attribute):
                                        bases.append(base.attr)
                                classes[name] = bases
                                for b in bases:
                                    parents.setdefault(b, []).append(name)

                    except:
                        pass

        report = []
        report.append("🦎✨ GECKONSTELACIÓN DE HERENCIAS\n")

        # Refactoreo por Ei2 para mayor impacto visual co Unicodes
        if not parents:
            report.append("\nNo se detectaron jerarquías de herencia.")
            return "\n".join(report)

        for parent in sorted(parents):  # Ordenamos para que sea coherente
            report.append(f"\n⭐ {parent}")
            
            children_list = parents[parent]
            total_children = len(children_list)

            for i, child in enumerate(children_list):
                # Si 'i' es el índice del último elemento, usamos el cierre
                is_last = (i == total_children - 1)
                connector = "└── " if is_last else "├── "
                
                report.append(f"   {connector}{child}")

        return "\n".join(report)

# ---------------------------
# GUI
# ---------------------------
class GeckodeSniferWindow(QMainWindow):
    def __init__(self):

        super().__init__()
        self.geckoversion = "🦎 GeckodeSnifer™ 4.1"
        self.setWindowTitle(f"{self.geckoversion}")
        self.resize(1200, 800)

        # Icono de aplicación
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        self.IconPath = os.path.join(scriptDir, 'icons')   
        self.setWindowIcon(QtGui.QIcon(self.IconPath + os.path.sep + 'geckodesniferdark.png'))

        # Aprovechamos la ruta para aplicarla al path al menos al inicio
        self.path = scriptDir

        self.init_ui()

        QTimer.singleShot(800, self.warm_up_and_autocheq)

    def init_ui(self):
        
        # Status Bar (El Bar de los estados alterados de consciencia)
        self.status_label = QLabel("🦎 GeckodeSnifer Status: idle")
        self.status_label.setStyleSheet("font-size: 14px; font-weight: bold; color: #2ecc71;")
        self.status_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)

        self.statusBar().show() # Asegura que sea visible
        self.statusBar().setStyleSheet("color: #2ecc71; font-weight: bold; font-size: 14px;")
        self.statusBar().showMessage(f" {self.geckoversion} ")
        self.statusBar().addPermanentWidget(self.status_label)

        # Tool Bar (El Bar donde se emborrachan los botones)
        toolbar = QToolBar("Gecko Control Panel")
        toolbar.setMovable(False)           # Para que no la arrastren por ahí
        toolbar.setFloatable(False)
        toolbar.setMinimumHeight(70)
        # Opcional: estilo de botones (texto debajo del ícono, o solo texto grande)
        toolbar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)  # o ToolButtonTextUnderIcon
        # Aumentamos tamaño de íconos (si después agregás icons, se nota)
        toolbar.setIconSize(QSize(32, 32))  # 24x24 es default, 32x32 ya se ve más pro

        select_folder = QAction("Select Folder of Proyect", self)
        select_folder.triggered.connect(self.select_folder)
        toolbar.addAction(select_folder)

        select_file = QAction("Select Individual File", self)
        select_file.triggered.connect(self.select_file)
        toolbar.addAction(select_file)

        sniff = QAction("GeckodeSnifiar con de Todo", self)
        sniff.triggered.connect(self.run_sniff)
        toolbar.addAction(sniff)

        # Personalizacion de Botones de toolbar por Ei2
        # 1. Buscas el widget asociado a esa acción específica
        btn_sniff = toolbar.widgetForAction(sniff)
        # 2. Le das personalidad digital
        if btn_sniff:
            self.set_ketul_button_colours(
                btn_sniff, 
                "#2ecc71", # Verde base
                "#27ae60", # Verde hover
                "#1e8449"  # Verde press
            )

        self.addToolBar(Qt.BottomToolBarArea, toolbar)

        # Tabs (Solapas para todos los Reportes Multiversales de 🦎 GeckodeSnifer)
        self.tabs = QTabWidget()
        self.tabs.setTabPosition(QTabWidget.North) # South, West, East, North
        
        self.tabs.setStyleSheet("""
            QTabBar::tab {
                /*font-size: 12px;                 /* Tamaño del texto (obvio / ver porque recorta texto al principio y final) */
                /*font-weight: bold;               /* Lo hace más visible (ver porque recorta texto al principio y final) */
                alignment: center;
                border-bottom-color: none;        /* Une la solapa con el panel */
                border-top-left-radius: 7px;      /* Bordes redondeados modernos */
                border-top-right-radius: 7px;
                padding: 7px 7px;                 /* Espacio interno Respira */
            }
            QTabBar::tab:selected {
                background: #19232d;              /* Fondo Negro como la NOche cuando está activa */
                color: #2ecc71;                   /* Verde Geckonico para resaltar */
                border-bottom: 2px solid #2ecc71; /* Verde Geckonico para resaltar */
            }
        """)

        self.sniff_text = QTextEdit()
        self.audit_text = QTextEdit()
        self.tree_text = QTextEdit()
        self.arch_text = QTextEdit()
        self.inherit_text = QTextEdit()
        self.doc_text = QTextEdit()
        self.dep_text = QTextEdit()
        self.rec_text = QTextEdit()
        
        self.tabs.addTab(self.wrap_tab(self.sniff_text, "Informe_GeckoSnifiado_X.txt"), "Sniff Report")
        self.tabs.addTab(self.wrap_tab(self.audit_text, "Auditoria_GeckoSnifiada_X.txt"), "Audit Report")
        self.tabs.addTab(self.wrap_tab(self.tree_text, "GeckoProjectTree_X.txt"), "Proyect Tree")
        self.tabs.addTab(self.wrap_tab(self.arch_text, "GeckoArchitectureMap_X.txt"), "Proyect Architecture Map")
        self.tabs.addTab(self.wrap_tab(self.inherit_text, "GeckoInheritanceConstellation_X.txt"), "Inheritance Constellation")
        self.tabs.addTab(self.wrap_tab(self.doc_text, "GeckoDocScore_X.txt"), "DocScore")
        self.tabs.addTab(self.wrap_tab(self.dep_text, "GeckoDependencies_X.txt"), "Dependencies Chequer")
        self.tabs.addTab(self.wrap_tab(self.rec_text, "GeckodeSnifer_Recommend_X.txt"), "GeckodeSnifer Recommendations")
        
        self.setCentralWidget(self.tabs)
        
    # QToolButton Color Set by Ei2
    def set_ketul_button_colours(self, ketulbutton, backcolour, hoverbackcolour, presscolour, textcolour="white"):
        """
        Aplica un estilo visual personalizado a un QToolButton de la toolbar.
        """
        if ketulbutton:
            ketulbutton.setStyleSheet(f"""
                QToolButton {{
                    background-color: {backcolour};
                    color: {textcolour};
                    font-weight: bold;
                    border-radius: 6px;
                    padding: 6px 12px;
                    margin: 2px;
                    border: 1px solid rgba(0, 0, 0, 0.1);
                }}
                QToolButton:hover {{
                    background-color: {hoverbackcolour};
                }}
                QToolButton:pressed {{
                    background-color: {presscolour};
                    border: 1px solid rgba(0, 0, 0, 0.3);
                }}
            """)
        ketulbutton.setMinimumWidth(ketulbutton.sizeHint().width() + 20)

    def wrap_tab(self, text_widget, default_name):

        widget = QWidget()
        layout = QVBoxLayout()

        layout.addWidget(text_widget)

        save_btn = QPushButton("Guardar Informe Geckonico")
        save_btn.clicked.connect(lambda: self.save_report(text_widget, default_name))

        layout.addWidget(save_btn)

        widget.setLayout(layout)

        return widget

    def select_folder(self):

        path = QFileDialog.getExistingDirectory(self, "Seleccionar carpeta")

        if path:
            self.path = path
            self.status_label.setText(f"🦎 Carpeta: {path}")

    def select_file(self):

        path, _ = QFileDialog.getOpenFileName(self, "Seleccionar archivo", "", "Python Files (*.py)")

        if path:
            self.path = path
            self.status_label.setText(f"🦎 Archivo: {path}")

    def warm_up_and_autocheq(self):
        """
        Gecko Footprint:
        Warm-up Geckoniano — GeckodeSnifer se analiza a sí mismo
        para verificar que el motor funciona correctamente.
        """

        try:

            self.status_label.setText(
                "🦎✨ Warm-up Gecko: auto-sniff en progreso..."
            )

            self_path = os.path.abspath(__file__)
            project = os.path.dirname(self_path)

            sniffer = GeckodeSnifer(project)

            sniff_report = sniffer.sniff_project()
            audit_report = sniffer.audit_project()
            dep_report, missing = sniffer.check_dependencies()

            warmup_report = (
                "🦎 GECKO WARMUP & AUTOCHECK\n\n"
                + sniff_report
                + "\n\n"
                + audit_report
                + "\n\n"
                + dep_report
            )

            # Mostrar en la pestaña Sniff
            self.sniff_text.setText(warmup_report)

            # Guardar informe
            with open("Informe_GeckoSnifiado_WarmUp.txt", "w", encoding="utf-8") as f:
                f.write(warmup_report)

            self.status_label.setText(
                "🦎 Warm-up completo ✔"
            )

        except Exception as e:

            self.status_label.setText(
                f"⚠ Error en Warm-up Gecko: {e}"
            )

    def run_sniff(self):

        if not self.path:
            self.status_label.setText("⚠ No hay ruta seleccionada")
            return

        if os.path.isfile(self.path):
            project = os.path.dirname(self.path)
        else:
            project = self.path

        sniffer = GeckodeSnifer(project)

        # 1 Sniffer principal
        sniff_report = sniffer.sniff_project()
        self.sniff_text.setText(sniff_report)

        # 2 Árbol del proyecto
        tree_report = sniffer.build_project_tree()
        self.tree_text.setText(tree_report)

        # 3 Gecko PAM (Proyect Arquitecture Map)
        arch_report = sniffer.build_architecture_map()
        self.arch_text.setText(arch_report)

        # 4 Geckonstellation (Inheritance Constellation) // Geckonstelación de Herencias 🦎✨.
        inherit_report = sniffer.build_inheritance_constellation()
        self.inherit_text.setText(inherit_report)

        # 5 Auditoría
        audit_report = sniffer.audit_project()
        self.audit_text.setText(audit_report)

        # 6 Dependencias
        dep_report, missing = sniffer.check_dependencies()
        self.dep_text.setText(dep_report)
        sniffer.missing_deps = missing

        # 7 Recomendaciones
        rec_report = sniffer.generate_recommendations()
        self.rec_text.setText(rec_report)

        # STATUS BAR
        score = sniffer.score
        files = sniffer.files
        warnings = sniffer.missing_docs + sniffer.large_files + sniffer.missing_deps

        bar = "█" * (score // 10) + "░" * (10 - score // 10)

        self.status_label.setText(
            f"🦎 GeckodeSnifer Status | DocScore {bar} {score}% | Files {files} | Warnings {warnings} | MissingDeps {sniffer.missing_deps}"
        )

        self.doc_text.setText(f"GECKO DOC SCORE\n{bar} {score}%")

    def save_report(self, text_widget, default_name):

        content = text_widget.toPlainText()

        path, _ = QFileDialog.getSaveFileName(
            self,
            "Guardar Informe Geckonico",
            default_name,
            "Text Files (*.txt)"
        )

        if path:

            with open(path, "w", encoding="utf-8") as f:
                f.write(content)

# ---------------------------
# MAIN
# ---------------------------
if __name__ == "__main__":

    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet(DarkPalette))

    window = GeckodeSniferWindow()
    window.show()

    sys.exit(app.exec_())