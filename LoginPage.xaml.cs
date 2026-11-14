namespace BibliotecaMovil;

public partial class LoginPage : ContentPage
{
    public LoginPage()
    {
        InitializeComponent();
    }

    private async void OnIniciarSesionClicked(object? sender, EventArgs e)
    {
        string usuario = TxtUsuario.Text?.Trim() ?? string.Empty;
        string pass = TxtPassword.Text?.Trim() ?? string.Empty;

        if (string.IsNullOrEmpty(usuario) || string.IsNullOrEmpty(pass))
        {
            await DisplayAlertAsync("Validación", "Por favor ingresa usuario y contraseña.", "Aceptar");
            return;
        }

        await DisplayAlertAsync("Bienvenido", $"¡Acceso concedido para {usuario}!\nRedirigiendo al Catálogo...", "Continuar");

        // Navegar a la pestaña del Catálogo
        await Shell.Current.GoToAsync("//CatalogoPage");
    }
}
