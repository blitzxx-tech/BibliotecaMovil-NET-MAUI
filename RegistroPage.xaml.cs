using BibliotecaMovil.Models;

namespace BibliotecaMovil;

public partial class RegistroPage : ContentPage
{
    public RegistroPage()
    {
        InitializeComponent();
    }

    private async void OnGuardarClicked(object? sender, EventArgs e)
    {
        if (string.IsNullOrWhiteSpace(TxtTitulo.Text) || string.IsNullOrWhiteSpace(TxtAutor.Text))
        {
            await DisplayAlertAsync("Validación", "Por favor ingresa al menos el título y el autor del libro.", "Entendido");
            return;
        }

        decimal.TryParse(TxtPrecio.Text, out decimal precio);

        var nuevoLibro = new Libro
        {
            Titulo = TxtTitulo.Text.Trim(),
            Autor = TxtAutor.Text.Trim(),
            Categoria = PickerCategoria.SelectedItem?.ToString() ?? "General",
            Precio = precio > 0 ? precio : 150.00m,
            EsNuevo = true,
            Imagen = "dotnet_bot.png"
        };

        // Agregar al repositorio en memoria compartido
        LibrosRepository.Libros.Add(nuevoLibro);

        LblMensaje.Text = $"✓ ¡El libro '{nuevoLibro.Titulo}' fue registrado exitosamente!";
        LblMensaje.IsVisible = true;

        bool irAlCatalogo = await DisplayAlertAsync("Éxito", $"Libro '{nuevoLibro.Titulo}' guardado correctamente.\n¿Deseas ir al Catálogo para visualizarlo?", "Ver Catálogo", "Quedarse");
        LimpiarCampos();

        if (irAlCatalogo)
        {
            await Shell.Current.GoToAsync("//CatalogoPage");
        }
    }

    private void OnLimpiarClicked(object? sender, EventArgs e)
    {
        LimpiarCampos();
        LblMensaje.IsVisible = false;
    }

    private void LimpiarCampos()
    {
        TxtTitulo.Text = string.Empty;
        TxtAutor.Text = string.Empty;
        TxtPrecio.Text = string.Empty;
        PickerCategoria.SelectedIndex = -1;
    }
}
