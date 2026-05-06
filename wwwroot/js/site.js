// SignalR Support Chat Logic
const connection = new signalR.HubConnectionBuilder()
    .withUrl("/supportHub")
    .build();

connection.on("ReceiveMessage", (user, message) => {
    const msgDiv = document.createElement("div");
    msgDiv.textContent = `${user}: ${message}`;
    document.getElementById("support-messages")?.appendChild(msgDiv);
});

connection.on("ReceiveNotification", (message) => {
    const adminNotifDiv = document.createElement("div");
    adminNotifDiv.textContent = `New Notification: ${message}`;
    document.getElementById("admin-notifications")?.appendChild(adminNotifDiv);
});

connection.start().catch(err => console.error(err.toString()));

document.getElementById("support-toggle")?.addEventListener("click", () => {
    document.getElementById("support-box").classList.toggle("d-none");
});

document.getElementById("support-close")?.addEventListener("click", () => {
    document.getElementById("support-box").classList.add("d-none");
});

document.getElementById("support-send")?.addEventListener("click", () => {
    const user = "User"; // In real app, get from Identity
    const message = document.getElementById("support-input").value;
    connection.invoke("SendMessage", user, message).catch(err => console.error(err.toString()));
    connection.invoke("NotifyAdmin", `User sent: ${message}`).catch(err => console.error(err.toString()));
    document.getElementById("support-input").value = "";
});
