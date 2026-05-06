using Microsoft.AspNetCore.Identity;
using Microsoft.Extensions.DependencyInjection;
using System;
using System.Threading.Tasks;
using Bervado.Web.Models;
using System.Linq;

namespace Bervado.Web.Data
{
    public static class DbSeeder
    {
        public static async Task SeedRolesAndAdminAsync(IServiceProvider serviceProvider)
        {
            using var scope = serviceProvider.CreateScope();
            var roleManager = scope.ServiceProvider.GetRequiredService<RoleManager<IdentityRole>>();
            var userManager = scope.ServiceProvider.GetRequiredService<UserManager<IdentityUser>>();
            var context = scope.ServiceProvider.GetRequiredService<ApplicationDbContext>();

            string[] roleNames = { "Admin", "Manager", "User" };
            foreach (var roleName in roleNames)
            {
                var roleExist = await roleManager.RoleExistsAsync(roleName);
                if (!roleExist)
                {
                    await roleManager.CreateAsync(new IdentityRole(roleName));
                }
            }

            var adminEmail = "admin@bervado.com";
            var adminUser = await userManager.FindByEmailAsync(adminEmail);
            if (adminUser == null)
            {
                adminUser = new IdentityUser
                {
                    UserName = adminEmail,
                    Email = adminEmail,
                    EmailConfirmed = true
                };
                var result = await userManager.CreateAsync(adminUser, "Admin123!");
                if (result.Succeeded)
                {
                    await userManager.AddToRoleAsync(adminUser, "Admin");
                }
            }

            if (!context.Products.Any())
            {
                context.Products.AddRange(
                    new Product
                    {
                        Title = "Classic Linen Shirt",
                        Price = 85.00M,
                        Description = "Crafted for everyday refinement. Lightweight, breathable, and timeless.",
                        ImageUrl = "https://images.unsplash.com/photo-1505022610485-0249ba5b3675?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3",
                        Sizes = "S, M, L, XL"
                    },
                    new Product
                    {
                        Title = "Tailored Wool Trousers",
                        Price = 120.00M,
                        Description = "Minimalist cut with a subtle drape. A foundation for any sophisticated wardrobe.",
                        ImageUrl = "https://images.unsplash.com/photo-1594633312681-425c7b97ccd1?w=500&auto=format&fit=crop&q=60",
                        Sizes = "30, 32, 34, 36"
                    },
                    new Product
                    {
                        Title = "Cashmere Blend Polo",
                        Price = 145.00M,
                        Description = "Soft, understated, and incredibly comfortable. Perfect for layering or wearing on its own.",
                        ImageUrl = "https://images.unsplash.com/photo-1601333144130-8cbb312386b6?w=500&auto=format&fit=crop&q=60",
                        Sizes = "M, L, XL"
                    },
                    new Product
                    {
                        Title = "Signature Leather Belt",
                        Price = 65.00M,
                        Description = "Full-grain leather with a brushed gold-tone buckle. The ultimate quiet luxury accessory.",
                        ImageUrl = "https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=500&auto=format&fit=crop&q=60",
                        Sizes = "32, 34, 36, 38"
                    }
                );
                await context.SaveChangesAsync();
            }
        }
    }
}
