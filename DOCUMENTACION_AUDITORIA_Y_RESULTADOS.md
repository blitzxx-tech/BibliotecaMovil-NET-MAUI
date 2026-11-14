# UTSJR | UAJ - Unidad Académica Jalpan
## Ingeniería en Desarrollo y Gestión de Software (IDyGS)
### Asignatura: Desarrollo de Aplicaciones Móviles Multiplataforma
---

# REPORTE DE LABORATORIO Y AUDITORÍA TÉCNICA
## Proyecto: "Biblioteca Móvil" en .NET MAUI 10
**Diseño de Interfaces Multiplataforma con Layouts Avanzados**

---

## 1. Resumen Ejecutivo y Propósito Didáctico

El presente proyecto implementa la propuesta didáctica del **Laboratorio de 60 minutos** (página 20 de la presentación institucional), cuyo objetivo es diseñar y construir una aplicación interactiva y responsiva denominada **"Biblioteca Móvil"** sobre el framework **.NET MAUI 10** en **C# y XAML**.

La evidencia de aprendizaje exige integrar de manera justificada y funcional los contenedores de diseño (*Layouts*) fundamentales de .NET MAUI, cubriendo:
1. **VerticalStackLayout / StackLayout**: Estructuración secuencial y formularios limpios.
2. **HorizontalStackLayout**: Barras de botones de acción y agrupaciones horizontales.
3. **Grid**: Alineación precisa matricial de filas/columnas para captura de datos y composición de tarjetas.
4. **FlexLayout**: Filtros de categorías con ajuste de línea automático (*Wrap*) y alineación fluida.
5. **AbsoluteLayout**: Posicionamiento libre por coordenadas \((X, Y)\) para la pantalla de inicio de sesión (*Login*) y superposición de insignias flotantes (*badges* como "NUEVO").
6. **BindableLayout**: Generación dinámica de plantillas enlazadas a datos sin sobrecarga de controles pesados.
7. **Diseños Personalizados y Recursos Globales**: Estandarización visual con `ResourceDictionary`, paleta de colores institucional y estilos reutilizables (`Styles.xaml`).

---

## 2. Auditoría Técnica de Código y Resoluciones

Durante el proceso de auditoría y revisión estricta de la solución, se evaluaron los componentes en las plataformas **Windows (WinUI 3 / net10.0-windows10.0.19041.0)** y **Android (net10.0-android)**:

### Hallazgo 1: Obsolescencia en API de Diálogos (.NET MAUI 10)
* **Diagnóstico**: Se detectaron 14 advertencias de compilador tipo `CS0618` debido a que el método sincrónico clásico `Page.DisplayAlert(...)` ha sido formalmente marcado como obsoleto en la versión 10 de .NET MAUI en favor del patrón asíncrono explícito.
* **Resolución**: Se refactorizaron todos los controladores en `LoginPage.xaml.cs`, `CatalogoPage.xaml.cs` y `RegistroPage.xaml.cs` adoptando `await DisplayAlertAsync(...)`. 
* **Resultado**: **0 Errores, 0 Advertencias**.

### Hallazgo 2: Cobertura Completa de los 7 Layouts de la Presentación
* **Diagnóstico**: La solución inicial contaba con el formulario de registro (`RegistroPage`) y el catálogo (`CatalogoPage`), pero no implementaba la pantalla dedicada de Login explicada en las páginas 11 y 12 mediante `AbsoluteLayout`.
* **Resolución**: Se desarrolló e integró `LoginPage.xaml` y `LoginPage.xaml.cs` empleando las coordenadas y dimensiones de la especificación didáctica (Logo, campos de entrada con `ClearButtonVisibility`, contraseña segura y botón de acceso directo).
* **Navegación**: Se actualizó `AppShell.xaml` con 3 pestañas principales: **Login**, **Catálogo** y **Registrar**.

### Hallazgo 3: Interactividad y Filtros en Tiempo Real
* **Diagnóstico**: La diapositiva 20 mostraba una barra de búsqueda (`🔍 Buscar libro...`) y chips de categorías, pero no existía filtrado combinado ni retroalimentación visual de qué chip estaba seleccionado.
* **Resolución**:
  - Se incorporó un control `SearchBar` en `CatalogoPage.xaml` conectado al evento `OnBuscarTextChanged`.
  - Se implementó un algoritmo de búsqueda insensible a mayúsculas/minúsculas que combina categoría activa + texto de búsqueda por título o autor.
  - Se programó en C# la alternancia dinámica de color de los chips en el `FlexLayout`, resaltando el botón activo en azul primario (`#2563EB`) y retornando los demás a gris neutro (`#E2E8F0`).

### Hallazgo 4: Estilos Globales Centralizados
* **Diagnóstico**: Los estilos de botones y bordes estaban repetidos de forma local.
* **Resolución**: Se ampliaron `Resources/Styles/Colors.xaml` y `Resources/Styles/Styles.xaml` con los recursos institucionales solicitados en las diapositivas 15 y 16 (`BtnPrincipal`, `BtnSecundario`, `CardCustom`, `Primario`, `Secundario`).

---

## 3. Matriz de Layouts Implementados y Justificación Técnica

| Layout | Archivo XAML | Propósito en la App | Justificación y Buenas Prácticas |
| :--- | :--- | :--- | :--- |
| **AbsoluteLayout** | `LoginPage.xaml`<br>`CatalogoPage.xaml` | - Pantalla de Login con coordenadas fijas (diapos 11-12).<br>- Insignia roja flotante **"NUEVO"** superpuesta en la portada del libro. | Máxima libertad de posición para elementos decorativos o insignias superpuestas sin alterar el flujo del resto de componentes. |
| **Grid** | `RegistroPage.xaml`<br>`CatalogoPage.xaml` | - Formulario de captura (2 columnas: etiquetas y campos).<br>- Tarjeta de libro (Columna 0: portada de 90px, Columna 1: datos en `*`). | Estructura rígida y ordenada de filas y columnas. Es el contenedor más eficiente para formularios alineados. |
| **VerticalStackLayout** | `RegistroPage.xaml`<br>`LoginPage.xaml` | Contenedor principal que organiza verticalmente el encabezado, formulario y botones. | Especializado para una sola dimensión vertical; más liviano y de mayor rendimiento que el antiguo `StackLayout`. |
| **HorizontalStackLayout** | `CatalogoPage.xaml`<br>`RegistroPage.xaml` | - Barra de acciones superior (Agregar, Editar, Eliminar, Refrescar).<br>- Botones del formulario (Guardar y Limpiar). | Distribuye controles contiguos en una fila sin recalcular anchos complejos innecesarios. |
| **FlexLayout** | `CatalogoPage.xaml` | Barra de filtros de categoría tipo "Chips" con propiedad `Wrap="Wrap"`. | Permite salto de línea fluido cuando la pantalla del teléfono o ventana de Windows cambia de tamaño. |
| **BindableLayout** | `CatalogoPage.xaml` | Enlace de datos de la lista `LibrosFiltrados` sobre un `VerticalStackLayout`. | Ideal para catálogos pequeños o medianos; elimina el overhead de virtualización pesada cuando se usa con colecciones ligeras. |
| **Diseños Personalizados** | `Styles.xaml` | Estilos `BtnPrincipal`, `CardCustom` y paleta de colores corporativa. | Reutilización de estilos globales garantizando consistencia visual (UI/UX) y facilidad de mantenimiento. |

---

## 4. Estructura del Proyecto

```text
BibliotecaMovil/
├── Models/
│   ├── Categorias.cs         # Lista maestra de categorías (Tecnología, IA, Novela, etc.)
│   ├── Libro.cs              # Entidad Libro (Título, Autor, Categoría, Precio, Imagen, EsNuevo)
│   └── LibrosRepository.cs   # Repositorio en memoria con datos precargados observables
├── Platforms/
│   ├── Android/              # Configuración y manifiesto nativo Android
│   └── Windows/              # Configuración WinUI 3 y Package.appxmanifest
├── Resources/
│   ├── Images/dotnet_bot.png # Recurso gráfico de soporte y portadas
│   └── Styles/
│       ├── Colors.xaml       # Paleta cromática oficial (Primario, Secundario, Gris, etc.)
│       └── Styles.xaml       # Diccionario de estilos (BtnPrincipal, CardCustom, etc.)
├── App.xaml / App.xaml.cs    # Inicialización de la aplicación y recursos globales
├── AppShell.xaml / cs        # Navegación por pestañas (Login, Catálogo, Registrar)
├── LoginPage.xaml / cs       # Interfaz con AbsoluteLayout (Páginas 11-12)
├── CatalogoPage.xaml / cs    # Catálogo dinámico con Grid, FlexLayout, SearchBar y BindableLayout
├── RegistroPage.xaml / cs    # Formulario con VerticalStackLayout, Grid y validación
└── BibliotecaMovil.csproj    # Configuración de compilación multiplataforma .NET 10
```

---

## 5. Evidencias Visuales de la Aplicación en Ejecución (Fase 6)

Las siguientes capturas corresponden a la ejecución interactiva en Windows (WinUI 3):

### Figura 1: Pantalla de Login (`AbsoluteLayout`)
![Pantalla de Login](file:///C:/Users/Lenovo/Documents/INVESTIGAIONES/BibliotecaMovil/captura_login.png)
*Posicionamiento absoluto por coordenadas (X, Y), insignia superior derecha 'MAUI 10', encabezado institucional UTSJR - UAJ y formulario estilizado con alto contraste.*

### Figura 2: Pantalla de Catálogo (`Grid` + `FlexLayout` + `BindableLayout` + `AbsoluteLayout`)
![Pantalla de Catálogo](file:///C:/Users/Lenovo/Documents/INVESTIGAIONES/BibliotecaMovil/captura_catalogo.png)
*Barra de acciones (`HorizontalStackLayout`), buscador dinámico, chips de categoría en `FlexLayout` con salto de línea (Wrap) y tarjetas con división matricial (`Grid`) e insignia 'NUEVO'.*

### Figura 3: Pantalla de Registro de Libros (`VerticalStackLayout` + `Grid` + `HorizontalStackLayout`)
![Pantalla de Registro](file:///C:/Users/Lenovo/Documents/INVESTIGAIONES/BibliotecaMovil/captura_registro.png)
*Estructura de formulario con `Grid` alineado a 2 columnas (Título, Autor, Categoría Picker, Precio), contenedor `VerticalStackLayout` y botones 'Guardar Libro' / 'Limpiar' en `HorizontalStackLayout`.*

---

## 6. Instrucciones de Compilación y Ejecución

### Requisitos del Sistema
* .NET SDK 10 instalado con soporte de workloads MAUI (`maui-windows`, `maui-android`).
* Visual Studio 2022/2026 o CLI de .NET.

### Comandos de Ejecución desde Consola

1. **Ejecutar en Windows (Escritorio)**:
   ```powershell
   cd C:\Users\Lenovo\Documents\INVESTIGAIONES\BibliotecaMovil
   dotnet build -f net10.0-windows10.0.19041.0
   dotnet run -f net10.0-windows10.0.19041.0
   ```

2. **Compilar para Android**:
   ```powershell
   dotnet build -f net10.0-android
   ```

---

## 7. Conclusiones

1. **Cumplimiento de la Evidencia Didáctica**: La aplicación integra con éxito no solo los tres layouts mínimos solicitados por la propuesta didáctica, sino la totalidad de los 7 esquemas de contenedores presentados en la guía de la asignatura IDyGS.
2. **Eficiencia en Arquitectura XAML**: La separación clara entre la estructura matricial (`Grid`), el flujo lineal (`VerticalStackLayout` y `HorizontalStackLayout`) y la adaptabilidad fluida (`FlexLayout`) demuestra cómo optimizar el árbol visual de .NET MAUI sin penalizar los tiempos de renderizado.
3. **Calidad de Código y Modernización**: La auditoría permitió migrar la solución a las directivas actuales de .NET 10 (eliminando llamadas obsoletas a `DisplayAlert` por `DisplayAlertAsync`) logrando una compilación totalmente limpia.
