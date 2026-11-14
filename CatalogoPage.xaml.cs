using System.Collections.ObjectModel;
using BibliotecaMovil.Models;

namespace BibliotecaMovil;

public partial class CatalogoPage : ContentPage
{
    public ObservableCollection<Libro> LibrosFiltrados { get; } = new();
    private string categoriaActual = "Todos";
    private string textoBusqueda = string.Empty;

    public CatalogoPage()
    {
        InitializeComponent();
        BindingContext = this;
        ActualizarLista();
    }

    protected override void OnAppearing()
    {
        base.OnAppearing();
        ActualizarLista();
    }

    private void ActualizarLista()
    {
        LibrosFiltrados.Clear();
        foreach (var libro in LibrosRepository.Libros)
        {
            bool coincideCategoria = categoriaActual == "Todos" || libro.Categoria.Equals(categoriaActual, StringComparison.OrdinalIgnoreCase);
            bool coincideBusqueda = string.IsNullOrWhiteSpace(textoBusqueda) ||
                                     libro.Titulo.Contains(textoBusqueda, StringComparison.OrdinalIgnoreCase) ||
                                     libro.Autor.Contains(textoBusqueda, StringComparison.OrdinalIgnoreCase);

            if (coincideCategoria && coincideBusqueda)
            {
                LibrosFiltrados.Add(libro);
            }
        }
    }

    private void OnBuscarTextChanged(object? sender, TextChangedEventArgs e)
    {
        textoBusqueda = e.NewTextValue ?? string.Empty;
        ActualizarLista();
    }

    private void OnFiltroClicked(object? sender, EventArgs e)
    {
        if (sender is Button botonSeleccionado)
        {
            categoriaActual = botonSeleccionado.Text;

            // Actualizar estilo visual de los botones del filtro (Chip seleccionado vs no seleccionado)
            foreach (var elemento in FlexCategorias.Children)
            {
                if (elemento is Button btn)
                {
                    if (btn == botonSeleccionado)
                    {
                        btn.BackgroundColor = Color.FromArgb("#2563EB");
                        btn.TextColor = Colors.White;
                    }
                    else
                    {
                        btn.BackgroundColor = Color.FromArgb("#E2E8F0");
                        btn.TextColor = Color.FromArgb("#1E293B");
                    }
                }
            }

            ActualizarLista();
        }
    }

    private async void OnAgregarAccionClicked(object? sender, EventArgs e)
    {
        await Shell.Current.GoToAsync("//RegistroPage");
    }

    private async void OnEditarAccionClicked(object? sender, EventArgs e)
    {
        await DisplayAlertAsync("Editar", "Selecciona o abre el formulario de registro para agregar o modificar libros.", "Aceptar");
    }

    private async void OnEliminarAccionClicked(object? sender, EventArgs e)
    {
        if (LibrosFiltrados.Count > 0)
        {
            var ultimo = LibrosFiltrados[^1];
            bool confirmar = await DisplayAlertAsync("Eliminar", $"¿Deseas eliminar el libro '{ultimo.Titulo}'?", "Sí, eliminar", "Cancelar");
            if (confirmar)
            {
                LibrosRepository.Libros.Remove(ultimo);
                ActualizarLista();
            }
        }
        else
        {
            await DisplayAlertAsync("Aviso", "No hay libros en esta categoría para eliminar.", "Aceptar");
        }
    }

    private void OnRefrescarClicked(object? sender, EventArgs e)
    {
        TxtBuscar.Text = string.Empty;
        textoBusqueda = string.Empty;
        categoriaActual = "Todos";

        // Resetear visualmente chips a "Todos"
        foreach (var elemento in FlexCategorias.Children)
        {
            if (elemento is Button btn)
            {
                if (btn.Text == "Todos")
                {
                    btn.BackgroundColor = Color.FromArgb("#2563EB");
                    btn.TextColor = Colors.White;
                }
                else
                {
                    btn.BackgroundColor = Color.FromArgb("#E2E8F0");
                    btn.TextColor = Color.FromArgb("#1E293B");
                }
            }
        }

        ActualizarLista();
    }
}
