document.addEventListener("DOMContentLoaded", function () {
    console.log("JavaScript Loaded Successfully! 🚀");

    // Add Hover Effect on List Items
    const listItems = document.querySelectorAll("li");
    listItems.forEach((item) => {
        item.addEventListener("mouseover", () => {
            item.style.backgroundColor = "#e3f2fd";
            item.style.transition = "background-color 0.3s ease";
        });

        item.addEventListener("mouseleave", () => {
            item.style.backgroundColor = "white";
        });
    });

    // Confirm Before Deleting an Expense/Income
    const deleteButtons = document.querySelectorAll(".delete");
    deleteButtons.forEach((button) => {
        button.addEventListener("click", (event) => {
            if (!confirm("Are you sure you want to delete this record?")) {
                event.preventDefault(); // Prevent deletion if user cancels
            }
        });
    });

    // Show Toast Message on Successful Action (Example)
    function showToast(message) {
        let toast = document.createElement("div");
        toast.innerText = message;
        toast.style.position = "fixed";
        toast.style.bottom = "20px";
        toast.style.left = "50%";
        toast.style.transform = "translateX(-50%)";
        toast.style.background = "#28a745";
        toast.style.color = "white";
        toast.style.padding = "10px 20px";
        toast.style.borderRadius = "5px";
        toast.style.boxShadow = "2px 2px 10px rgba(0,0,0,0.2)";
        document.body.appendChild(toast);
        
        setTimeout(() => {
            toast.remove();
        }, 3000);
    }

    // Example: Show toast when adding a new item
    const addItemForm = document.querySelector("#add-item-form");
    if (addItemForm) {
        addItemForm.addEventListener("submit", function () {
            showToast("Item added successfully! ✅");
        });
    }
});
