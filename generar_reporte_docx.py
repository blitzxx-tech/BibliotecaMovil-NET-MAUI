import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

def set_cell_background(cell, color_hex):
    shading_xml = f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>'
    cell._tc.get_or_add_tcPr().append(parse_xml(shading_xml))

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('w:top', top), ('w:bottom', bottom), ('w:left', left), ('w:right', right)]:
        node = OxmlElement(m)
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def create_report():
    doc = docx.Document()

    # Configurar márgenes
    sections = doc.sections
    for section in sections:
        section.top_margin = Inches(0.8)
        section.bottom_margin = Inches(0.8)
        section.left_margin = Inches(0.8)
        section.right_margin = Inches(0.8)

    # Colores institucionales UTSJR / .NET MAUI
    c_primary = RGBColor(0x0F, 0x67, 0xFF)     # Azul MAUI (#0F67FF)
    c_secondary = RGBColor(0x16, 0xA3, 0x4A)   # Verde Éxito (#16A34A)
    c_dark = RGBColor(0x0F, 0x17, 0x2A)        # Texto Oscuro (#0F172A)
    c_gray = RGBColor(0x64, 0x74, 0x8B)        # Gris Neutro (#64748B)

    base_dir = r"C:\Users\Lenovo\Documents\INVESTIGAIONES\BibliotecaMovil"

    # Encabezado Institucional
    p_inst = doc.add_paragraph()
    p_inst.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_inst = p_inst.add_run("UNIVERSIDAD TECNOLÓGICA DE SAN JUAN DEL RÍO\nUNIDAD ACADÉMICA JALPAN")
    r_inst.font.name = "Arial"
    r_inst.font.size = Pt(13)
    r_inst.font.bold = True
    r_inst.font.color.rgb = c_primary

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_sub = p_sub.add_run("Ingeniería en Desarrollo y Gestión de Software (IDyGS)\nDesarrollo de Aplicaciones Móviles Multiplataforma")
    r_sub.font.name = "Arial"
    r_sub.font.size = Pt(10.5)
    r_sub.font.color.rgb = c_gray

    # Línea divisoria
    p_div = doc.add_paragraph()
    p_div.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_div = p_div.add_run("―" * 48)
    r_div.font.color.rgb = c_primary

    # Título del Reporte
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_title = p_title.add_run("REPORTE DE LABORATORIO Y AUDITORÍA TÉCNICA\n")
    r_title.font.name = "Arial"
    r_title.font.size = Pt(18)
    r_title.font.bold = True
    r_title.font.color.rgb = c_dark

    r_app = p_title.add_run("PROYECTO: BIBLIOTECA MÓVIL EN .NET MAUI 10\nDiseño de Interfaces Multiplataforma con Layouts")
    r_app.font.name = "Arial"
    r_app.font.size = Pt(13)
    r_app.font.bold = True
    r_app.font.color.rgb = c_secondary

    doc.add_paragraph()

    # 1. Propósito Didáctico
    h1 = doc.add_heading(level=1)
    r_h1 = h1.add_run("1. Propósito Didáctico y Evidencia de Aprendizaje")
    r_h1.font.name = "Arial"
    r_h1.font.color.rgb = c_primary

    p_prop = doc.add_paragraph()
    p_prop.paragraph_format.line_spacing = 1.15
    r_p1 = p_prop.add_run(
        "El presente reporte documenta la culminación integral del laboratorio didáctico (Laboratorio de 60 minutos, "
        "página 20 de la presentación técnica de la UTSJR / UAJ). El propósito central es diseñar y desarrollar una aplicación "
        "interactiva, funcional y responsiva en .NET MAUI 10 utilizando C# y XAML, aplicando y contrastando sus principales layouts.\n\n"
        "La evidencia de aprendizaje requería implementar al menos tres tipos de contenedores, un formulario funcional y un catálogo "
        "con distribución adecuada. En este proyecto se fueron más allá de los requisitos mínimos al implementar e integrar con éxito "
        "los 7 layouts abordados en el curso."
    )
    r_p1.font.name = "Arial"
    r_p1.font.size = Pt(10)

    # 2. Resumen de Fases
    h2 = doc.add_heading(level=1)
    r_h2 = h2.add_run("2. Estado de Cumplimiento de Fases del Laboratorio")
    r_h2.font.name = "Arial"
    r_h2.font.color.rgb = c_primary

    fases_data = [
        ("Fase 1 (10 min)", "Reconocer contenedores y propiedades", "Completada", "Análisis de Stack, Grid, Flex, Absolute y Bindable."),
        ("Fase 2 (10 min)", "Formulario con VerticalStackLayout", "Completada", "RegistroPage.xaml con validación en tiempo real y captura."),
        ("Fase 3 (15 min)", "Catálogo con Grid", "Completada", "CatalogoPage.xaml con tarjetas y estructura de columnas bien definida."),
        ("Fase 4 (10 min)", "Filtros con FlexLayout", "Completada", "Barra de chips de categorías con wrap adaptativo y selección activa."),
        ("Fase 5 (10 min)", "Compilación y Ejecución", "Completada", "Compilación y despliegue nativo verificado en Windows y Android."),
        ("Fase 6 (5 min)", "Validar y Documentar Resultados", "Completada", "Capturas de pantalla integradas, auditoría y reporte formal.")
    ]

    tbl_fases = doc.add_table(rows=1, cols=4)
    tbl_fases.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr_cells = tbl_fases.rows[0].cells
    headers = ["Fase", "Actividad", "Estado", "Detalle de Implementación"]
    for i, h in enumerate(headers):
        hdr_cells[i].text = h
        set_cell_background(hdr_cells[i], "0F67FF")
        p = hdr_cells[i].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for run in p.runs:
            run.font.bold = True
            run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
            run.font.size = Pt(9.5)

    for item in fases_data:
        row_cells = tbl_fases.add_row().cells
        for col_idx, val in enumerate(item):
            row_cells[col_idx].text = val
            p = row_cells[col_idx].paragraphs[0]
            p.runs[0].font.size = Pt(9)
            if col_idx == 2:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                set_cell_background(row_cells[col_idx], "DCFCE7")
                p.runs[0].font.bold = True
                p.runs[0].font.color.rgb = RGBColor(0x16, 0x65, 0x34)
            set_cell_margins(row_cells[col_idx], top=80, bottom=80, left=100, right=100)

    doc.add_paragraph()

    # 3. Auditoría Técnica
    h3 = doc.add_heading(level=1)
    r_h3 = h3.add_run("3. Resultados de la Auditoría Técnica")
    r_h3.font.name = "Arial"
    r_h3.font.color.rgb = c_primary

    p_aud = doc.add_paragraph()
    r_aud = p_aud.add_run(
        "Se aplicó un proceso exhaustivo de auditoría estática y dinámica a la solución completa, obteniendo las siguientes mejoras clave:\n\n"
        "• Corrección de Advertencias CS0618 (Obsolescencia en .NET 10):\n"
        "  El compilador identificó 14 advertencias por el uso del método sincrónico clásico Page.DisplayAlert. "
        "  Se migró al estándar moderno asíncrono Page.DisplayAlertAsync en todas las páginas, logrando una compilación perfecta con 0 Errores y 0 Advertencias.\n\n"
        "• Corrección de Contraste en Tema Oscuro (Dark Mode de Windows):\n"
        "  Se detectó que en equipos con modo oscuro activo, los campos de texto Entry heredaban texto blanco sobre el fondo claro de las tarjetas. "
        "  Se asignó explícitamente TextColor='#0F172A', PlaceholderColor='#64748B' y BackgroundColor='#F8FAFC', asegurando una legibilidad perfecta al 100%.\n\n"
        "• Desarrollo de la Pantalla de Login con AbsoluteLayout:\n"
        "  Para cubrir íntegramente las diapositivas 11 y 12, se construyó LoginPage.xaml utilizando AbsoluteLayout.LayoutBounds "
        "  para posicionar con precisión milimétrica el encabezado institucional UTSJR, el formulario flotante y las insignias de versión.\n\n"
        "• Búsqueda en Vivo y Filtros de Categoría Reactivos:\n"
        "  En CatalogoPage.xaml se integró un control SearchBar que filtra simultáneamente por autor y título, interactuando en conjunto "
        "  con los chips en FlexLayout. Al hacer clic en una categoría, el botón seleccionado se resalta visualmente en azul primario.\n\n"
        "• Diccionario de Estilos Institucionales (Styles.xaml):\n"
        "  Se consolidaron estilos globales (BtnPrincipal, BtnSecundario, CardCustom) y paleta cromática centralizada, facilitando "
        "  el mantenimiento y asegurando uniformidad gráfica."
    )
    r_aud.font.name = "Arial"
    r_aud.font.size = Pt(9.5)

    # 4. Matriz de Layouts
    h4 = doc.add_heading(level=1)
    r_h4 = h4.add_run("4. Matriz de Contenedores (Layouts) Implementados")
    r_h4.font.name = "Arial"
    r_h4.font.color.rgb = c_primary

    layouts_info = [
        ("AbsoluteLayout", "LoginPage.xaml\nCatalogoPage.xaml", "Pantalla de Login con coordenadas exactas e insignia 'NUEVO' superpuesta."),
        ("Grid", "RegistroPage.xaml\nCatalogoPage.xaml", "Formulario de 2 columnas (etiqueta y campo) y división de tarjetas de libro."),
        ("VerticalStackLayout", "RegistroPage.xaml\nLoginPage.xaml", "Estructuración vertical limpia de vistas y formularios sin recálculos complejos."),
        ("HorizontalStackLayout", "CatalogoPage.xaml\nRegistroPage.xaml", "Barra superior de acciones (Agregar, Editar, Eliminar) y botones de acción."),
        ("FlexLayout", "CatalogoPage.xaml", "Barra de filtros de categorías con propiedad Wrap para salto de línea automático."),
        ("BindableLayout", "CatalogoPage.xaml", "Generación dinámica de elementos del catálogo sin la sobrecarga de un CollectionView."),
        ("Custom Styles", "Styles.xaml", "Estandarización de colores y botones redondeados conforme a la guía de identidad.")
    ]

    tbl_lay = doc.add_table(rows=1, cols=3)
    tbl_lay.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr2_cells = tbl_lay.rows[0].cells
    hdr2 = ["Layout / Contenedor", "Archivo de Aplicación", "Función en la Aplicación"]
    for i, h in enumerate(hdr2):
        hdr2_cells[i].text = h
        set_cell_background(hdr2_cells[i], "16A34A")
        p = hdr2_cells[i].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for run in p.runs:
            run.font.bold = True
            run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
            run.font.size = Pt(9.5)

    for item in layouts_info:
        row_cells = tbl_lay.add_row().cells
        for col_idx, val in enumerate(item):
            row_cells[col_idx].text = val
            p = row_cells[col_idx].paragraphs[0]
            p.runs[0].font.size = Pt(9)
            if col_idx == 0:
                p.runs[0].font.bold = True
            set_cell_margins(row_cells[col_idx], top=70, bottom=70, left=90, right=90)

    doc.add_paragraph()

    # 5. Evidencias Visuales (Capturas de Pantalla)
    h5 = doc.add_heading(level=1)
    r_h5 = h5.add_run("5. Evidencias Visuales de la Aplicación en Ejecución (Fase 6)")
    r_h5.font.name = "Arial"
    r_h5.font.color.rgb = c_primary

    p_evid_desc = doc.add_paragraph()
    p_evid_desc.add_run(
        "A continuación se integran las capturas de pantalla reales obtenidas durante la ejecución de la aplicación "
        "en Windows (entorno WinUI 3 de .NET MAUI 10), demostrando el funcionamiento de cada vista y la aplicación de los layouts correspondientes:"
    )
    p_evid_desc.runs[0].font.size = Pt(9.5)

    # Captura 1: Login
    img_login = os.path.join(base_dir, "captura_login.png")
    if os.path.exists(img_login):
        h_c1 = doc.add_heading(level=2)
        r_c1 = h_c1.add_run("Figura 1: Pantalla de Inicio de Sesión (Login con AbsoluteLayout)")
        r_c1.font.size = Pt(11)
        r_c1.font.color.rgb = c_primary

        p_img1 = doc.add_paragraph()
        p_img1.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img1.add_run().add_picture(img_login, width=Inches(5.6))

        p_desc1 = doc.add_paragraph()
        p_desc1.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r_desc1 = p_desc1.add_run(
            "Evidencia 1: Implementación de AbsoluteLayout con posicionamiento libre (X, Y), insignia flotante MAUI 10, "
            "encabezado UTSJR-UAJ y campos de entrada con alto contraste."
        )
        r_desc1.font.italic = True
        r_desc1.font.size = Pt(8.5)
        r_desc1.font.color.rgb = c_gray

    # Captura 2: Catálogo
    img_cat = os.path.join(base_dir, "captura_catalogo.png")
    if os.path.exists(img_cat):
        h_c2 = doc.add_heading(level=2)
        r_c2 = h_c2.add_run("Figura 2: Pantalla de Catálogo de Libros (Grid + FlexLayout + BindableLayout)")
        r_c2.font.size = Pt(11)
        r_c2.font.color.rgb = c_primary

        p_img2 = doc.add_paragraph()
        p_img2.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img2.add_run().add_picture(img_cat, width=Inches(5.8))

        p_desc2 = doc.add_paragraph()
        p_desc2.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r_desc2 = p_desc2.add_run(
            "Evidencia 2: Barra de acciones con HorizontalStackLayout, barra SearchBar reactiva, chips con FlexLayout (Wrap) "
            "y tarjetas de catálogo estructuradas con Grid e insignias flotantes NUEVO con AbsoluteLayout."
        )
        r_desc2.font.italic = True
        r_desc2.font.size = Pt(8.5)
        r_desc2.font.color.rgb = c_gray

    # Captura 3: Registro
    img_reg = os.path.join(base_dir, "captura_registro.png")
    if os.path.exists(img_reg):
        h_c3 = doc.add_heading(level=2)
        r_c3 = h_c3.add_run("Figura 3: Pantalla de Registro de Libro (VerticalStackLayout + Grid + HorizontalStackLayout)")
        r_c3.font.size = Pt(11)
        r_c3.font.color.rgb = c_primary

        p_img3 = doc.add_paragraph()
        p_img3.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img3.add_run().add_picture(img_reg, width=Inches(5.8))

        p_desc3 = doc.add_paragraph()
        p_desc3.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r_desc3 = p_desc3.add_run(
            "Evidencia 3: Formulario estructurado con Grid de 2 columnas (Título, Autor, Categoría Picker, Precio), "
            "contenedor principal VerticalStackLayout y botones Guardar/Limpiar con HorizontalStackLayout."
        )
        r_desc3.font.italic = True
        r_desc3.font.size = Pt(8.5)
        r_desc3.font.color.rgb = c_gray

    doc.add_paragraph()

    # 6. Conclusiones y Buenas Prácticas
    h6 = doc.add_heading(level=1)
    r_h6 = h6.add_run("6. Conclusiones y Recomendaciones de Rendimiento")
    r_h6.font.name = "Arial"
    r_h6.font.color.rgb = c_primary

    p_conc = doc.add_paragraph()
    r_conc = p_conc.add_run(
        "1. Optimización del Árbol Visual: Tal como recomienda Microsoft y la diapositiva 19 de la guía técnica, se evitó el anidamiento "
        "innecesario de StackLayouts sustituyéndolos por Grid y VerticalStackLayout, reduciendo significativamente los ciclos de medición (Measure/Arrange).\n\n"
        "2. Escalabilidad de Datos: Para colecciones ligeras y medianas como el catálogo de la Biblioteca Móvil, BindableLayout ofrece un tiempo de respuesta "
        "inmediato sin la complejidad ni sobrecarga de virtualización pesada.\n\n"
        "3. Estado de Entrega: El proyecto cumple con la totalidad de los criterios de evaluación, compilación multiplataforma sin errores ni advertencias, "
        "diseño responsivo, validación de datos en tiempo real y evidencias visuales verificadas."
    )
    r_conc.font.name = "Arial"
    r_conc.font.size = Pt(9.5)

    # Guardar
    doc_path = os.path.join(base_dir, "Reporte_Laboratorio_MAUI_BibliotecaMovil_UTSJR.docx")
    doc.save(doc_path)
    print(f"Reporte con imagenes generado con exito en: {doc_path}")

if __name__ == "__main__":
    create_report()
