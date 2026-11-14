using System.Collections.ObjectModel;

namespace BibliotecaMovil.Models;

public static class LibrosRepository
{
    public static ObservableCollection<Libro> Libros { get; } = new()
    {
        new Libro
        {
            Titulo = "Programación C# 12 y .NET 10",
            Autor = "Ana Torres",
            Categoria = "Tecnología",
            Precio = 450.00m,
            EsNuevo = true
        },
        new Libro
        {
            Titulo = "Bases de Datos Relacionales y NoSQL",
            Autor = "Carlos Mendoza",
            Categoria = "Bases de Datos",
            Precio = 380.00m,
            EsNuevo = false
        },
        new Libro
        {
            Titulo = "Inteligencia Artificial Práctica",
            Autor = "Roberto Gómez",
            Categoria = "IA",
            Precio = 520.00m,
            EsNuevo = true
        },
        new Libro
        {
            Titulo = "El Principito",
            Autor = "Antoine de Saint-Exupéry",
            Categoria = "Novela",
            Precio = 180.00m,
            EsNuevo = false
        },
        new Libro
        {
            Titulo = "Sistemas Operativos Modernos",
            Autor = "Andrew S. Tanenbaum",
            Categoria = "Ciencia",
            Precio = 610.00m,
            EsNuevo = false
        }
    };
}
