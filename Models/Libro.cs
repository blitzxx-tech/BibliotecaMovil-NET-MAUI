namespace BibliotecaMovil.Models;

public class Libro
{
    public string Titulo { get; set; } = string.Empty;
    public string Autor { get; set; } = string.Empty;
    public string Categoria { get; set; } = string.Empty;
    public decimal Precio { get; set; }
    public string Imagen { get; set; } = "dotnet_bot.png";
    public bool EsNuevo { get; set; } = true;
}
