using Microsoft.AspNetCore.SignalR;
using System.Threading.Tasks;

namespace Bervado.Web.Hubs
{
    public class SupportHub : Hub
    {
        public async Task SendMessage(string user, string message)
        {
            await Clients.All.SendAsync("ReceiveMessage", user, message);
        }

        public async Task NotifyAdmin(string message)
        {
            // Usually we would send this to users in the "Admin" role or a specific group.
            await Clients.Group("Admins").SendAsync("ReceiveNotification", message);
        }

        public override async Task OnConnectedAsync()
        {
            if (Context.User != null && Context.User.IsInRole("Admin"))
            {
                await Groups.AddToGroupAsync(Context.ConnectionId, "Admins");
            }
            await base.OnConnectedAsync();
        }

        public override async Task OnDisconnectedAsync(System.Exception? exception)
        {
            if (Context.User != null && Context.User.IsInRole("Admin"))
            {
                await Groups.RemoveFromGroupAsync(Context.ConnectionId, "Admins");
            }
            await base.OnDisconnectedAsync(exception);
        }
    }
}
