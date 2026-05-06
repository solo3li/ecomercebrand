using System.ComponentModel.DataAnnotations;

namespace Bervado.Web.Models
{
    public class Product
    {
        public int Id { get; set; }

        [Required, MaxLength(100)]
        public string Title { get; set; } = string.Empty;

        [Required]
        public decimal Price { get; set; }

        public string Description { get; set; } = string.Empty;

        public string ImageUrl { get; set; } = string.Empty;

        public string Sizes { get; set; } = string.Empty; // e.g., "S,M,L,XL"
    }
}
