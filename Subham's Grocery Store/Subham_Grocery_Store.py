# Subham's Fresh Grocery Store - a py project of Saksham Sharma AKA UnExplainableFish52
"""Features
    - Fully Controlled Customer Navigation from entering into the Shop to Checkout,
    - Optimal, Practical & Efficient techniques for the flawless execution of the program,
    - Input validations, well-controlled user flow,
    - Complete Shopping in one go,
    - Simple Tkinter GUI for easier navigation and Project Demonstration,
    - Fully Implemented using Classes and Functions only, 
    - Fine tuned using Claude Sonnet 4
"""
# Here we goo!!
# importing tkinter and GUI designing
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class SimpleGroceryStoreGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.setup_window()
        self.setup_data()
        self.setup_variables()
        self.create_welcome_screen()
        
    def setup_window(self):
        """Configure main window"""
        self.root.title("Subham's Fresh Store")
        self.root.geometry("800x600")
        self.root.configure(bg='#2d2d2d')
        
    def setup_data(self):
        """ This is the optimal way to initialize variables as they are easier to access and work with like this """
        self.products = {
            "Veggies": {
                1: {"name": "Potatoes", "price": 80},
                2: {"name": "Cucumbers", "price": 130},
                3: {"name": "Onions", "price": 160}
            },
            "Snacks": {
                1: {"name": "Bread", "price": 20},
                2: {"name": "Milk", "price": 50},
                3: {"name": "Chocolate", "price": 100}
            },
            "Meats & Fishes": {
                1: {"name": "Chicken", "price": 150},
                2: {"name": "Beef", "price": 250},
                3: {"name": "Fish", "price": 300}
            }
        }
        
    def setup_variables(self):
        """ Initializing Cart list to hold all the cart items until checkout"""
        self.cart_items = []
        
    def clear_screen(self):
        """Clear all widgets from screen, Tkinter stuff """
        for widget in self.root.winfo_children():
            widget.destroy()
            
    def create_welcome_screen(self):
        """Creating Welcome Screen, this is AI generated BTW , I am not this good at Tkinter"""
        self.clear_screen()
        
        # Welcome to Subham's Fresh Store!  YAY!!
        welcome_label = tk.Label(self.root, 
                                text="Welcome to Subham's Fresh Store",
                                font=('Arial', 26, 'bold'),
                                fg="#00fffb", bg="#3b1717")
        welcome_label.pack(pady=50)

        info_label = tk.Label(self.root,
                             text="We offer Vegetables, Meat, Eggs & Fish!",
                             font=('Arial', 18),
                             fg='lightblue', bg='#2d2d2d')
        info_label.pack(pady=20)
        
        # Controlling User Entry to the Store, Entry/Exit Point 
        start_btn = tk.Button(self.root,
                             text=" Let's Start Shopping",
                             font=('Arial', 16),
                             bg='green', fg='yellow',
                             width=20, height=2,
                             command=self.show_main_menu)
        start_btn.pack(pady=10)
        
        exit_btn = tk.Button(self.root,
                            text="I don't want to shop",
                            font=('Arial', 16),
                            bg="#bc0b0b", fg='yellow',
                            width=20, height=2,
                            command=self.exit_store)
        exit_btn.pack(pady=10)
        
    def show_main_menu(self):
        self.clear_screen()
        
        # Title
        title_label = tk.Label(self.root,
                              text="MAIN MENU",
                              font=('Arial', 18, 'bold'),
                              fg="#52f8fa", bg="#732323")
        title_label.pack(pady=30)
        
        # Guidance Menu to Control the User's Flow , Simple English
        instruction_label = tk.Label(self.root,
                                   text="Here is the guidance menu, please follow accordingly!",
                                   font=('Arial', 12),
                                   fg='lightgray', bg='#2d2d2d')
        instruction_label.pack(pady=10)
        
        # Menu buttons - exactly as in console
        veggies_btn = tk.Button(self.root,
                               text="1: Shop Veggies",
                               font=('Arial', 14),
                               bg="#261f1f", fg="#e1f33f",
                               width=25, height=2,
                               command=lambda: self.show_category("Veggies"))
        veggies_btn.pack(pady=5)
        
        snacks_btn = tk.Button(self.root,
                              text="2: Shop Snacks",
                              font=('Arial', 14),
                              bg='#261f1f', fg='#e1f33f',
                              width=25, height=2,
                              command=lambda: self.show_category("Snacks"))
        snacks_btn.pack(pady=5)
        
        meat_btn = tk.Button(self.root,
                            text="3: Shop Meats & Fishes",
                            font=('Arial', 14),
                            bg='#261f1f', fg='#e1f33f',
                            width=25, height=2,
                            command=lambda: self.show_category("Meats & Fishes"))
        meat_btn.pack(pady=5)
        
        checkout_btn = tk.Button(self.root,
                                text="4: Proceed to Checkout!",
                                font=('Arial', 14),
                                bg='#261f1f', fg='#e1f33f',
                                width=25, height=2,
                                command=self.checkout)
        checkout_btn.pack(pady=5)
        
        # Back to welcome
        back_btn = tk.Button(self.root,
                            text="Back to Welcome Menu",
                            font=('Arial', 12),
                            bg='#261f1f', fg='#e1f33f',
                            width=20, height=1,
                            command=self.create_welcome_screen)
        back_btn.pack(pady=20)
        
    def show_category(self, category_name):
        """Show category products - exact replica of console version"""
        self.clear_screen()
        
        # Category title
        title_label = tk.Label(self.root,
                              text=f"Welcome to {category_name} Section!!",
                              font=('Arial', 16, 'bold'),
                              fg="#02b0f6", bg="#000000")
        title_label.pack(pady=20)
        
        # Products header
        header_label = tk.Label(self.root,
                               text="SN : Item                Price per KG in Rupees:",
                               font=('Arial', 12, 'bold'),
                               fg='lightblue', bg='#2d2d2d')
        header_label.pack(pady=10)
        
        # Products list
        for item_id, item_info in self.products[category_name].items():
            product_text = f"{item_id}: {item_info['name']}                {item_info['price']}"
            
            product_btn = tk.Button(self.root,
                                   text=product_text,
                                   font=('Arial', 12),
                                   bg='lightblue', fg='black',
                                   width=40, height=1,
                                   command=lambda id=item_id, cat=category_name: self.select_product(cat, id))
            product_btn.pack(pady=2)
        
        # Continue shopping question
        continue_label = tk.Label(self.root,
                                 text=f"Select a product or go back to add more {category_name}",
                                 font=('Arial', 10),
                                 fg='yellow', bg='#2d2d2d')
        continue_label.pack(pady=20)
        
        # Navigation buttons
        back_btn = tk.Button(self.root,
                            text="Back to Main Menu",
                            font=('Arial', 12),
                            bg='gray', fg='white',
                            width=20, height=2,
                            command=self.show_main_menu)
        back_btn.pack(pady=10)
        
    def select_product(self, category_name, product_id):
        """Product selection and quantity input"""
        self.clear_screen()
        
        product_info = self.products[category_name][product_id]
        
        # Product selection confirmation
        title_label = tk.Label(self.root,
                              text=f"You selected {product_info['name']}",
                              font=('Arial', 16, 'bold'),
                              fg='white', bg='#2d2d2d')
        title_label.pack(pady=30)
        
        price_label = tk.Label(self.root,
                              text=f"Price: ₹{product_info['price']} per kg",
                              font=('Arial', 14),
                              fg='lightgreen', bg='#2d2d2d')
        price_label.pack(pady=10)
        
        # Quantity input
        qty_label = tk.Label(self.root,
                            text="Your desired quantity (kg):",
                            font=('Arial', 12),
                            fg='white', bg='#2d2d2d')
        qty_label.pack(pady=10)
        
        self.qty_var = tk.StringVar(value="1")
        qty_entry = tk.Entry(self.root,
                            textvariable=self.qty_var,
                            font=('Arial', 14),
                            width=10,
                            justify='center')
        qty_entry.pack(pady=10)
        
        # Add to cart button
        add_btn = tk.Button(self.root,
                           text="Add to Cart",
                           font=('Arial', 14),
                           bg='green', fg='white',
                           width=15, height=2,
                           command=lambda: self.add_to_cart(product_info, category_name))
        add_btn.pack(pady=20)
        
        # Navigation
        back_btn = tk.Button(self.root,
                            text=f"Back to {category_name}",
                            font=('Arial', 12),
                            bg='gray', fg='white',
                            width=20, height=1,
                            command=lambda: self.show_category(category_name))
        back_btn.pack(pady=10)
        
    def add_to_cart(self, product_info, category_name):
        """Add product to cart with validation"""
        try:
            quantity = int(self.qty_var.get())
            if quantity <= 0:
                messagebox.showerror("Invalid Quantity", "Please enter a quantity greater than 0")
                return
                
            total_cost = quantity * product_info['price']
            
            # Check if item already in cart
            for item in self.cart_items:
                if item["name"] == product_info["name"]:
                    item["quantity"] += quantity
                    item["total"] += total_cost
                    messagebox.showinfo("Updated Cart", 
                                      f"Updated {product_info['name']} in cart!\n"
                                      f"New quantity: {item['quantity']} kg\n"
                                      f"This purchase costs: ₹{total_cost}")
                    self.ask_continue_shopping(category_name)
                    return
            
            # Add new item
            self.cart_items.append({
                "name": product_info["name"],
                "quantity": quantity,
                "price_per_kg": product_info["price"],
                "total": total_cost
            })
            
            messagebox.showinfo("Added to Cart", 
                              f"Added {quantity} kg of {product_info['name']} to cart!\n"
                              f"This purchase costs: ₹{total_cost}")
            
            self.ask_continue_shopping(category_name)
            
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number for quantity")
            
    def ask_continue_shopping(self, category_name):
        """Ask if user wants to continue shopping in category"""
        self.clear_screen()
        
        # Question
        question_label = tk.Label(self.root,
                                 text=f"Do you want to add more items from {category_name}?",
                                 font=('Arial', 14),
                                 fg='white', bg='#2d2d2d')
        question_label.pack(pady=50)
        
        # Yes button
        yes_btn = tk.Button(self.root,
                           text="1 - Yes, continue shopping",
                           font=('Arial', 12),
                           bg='green', fg='white',
                           width=25, height=2,
                           command=lambda: self.show_category(category_name))
        yes_btn.pack(pady=10)
        
        # No button
        no_btn = tk.Button(self.root,
                          text="0 - No, go to main menu",
                          font=('Arial', 12),
                          bg='red', fg='white',
                          width=25, height=2,
                          command=self.show_main_menu)
        no_btn.pack(pady=10)
        
    def checkout(self):
        """Handle checkout process"""
        if not self.cart_items:
            messagebox.showwarning("Empty Cart", "Your cart is empty! Please add some items first.")
            return
            
        self.show_receipt()
        
    def show_receipt(self):
        """Show detailed receipt"""
        self.clear_screen()
        
        # Receipt title
        title_label = tk.Label(self.root,
                              text="CHECKOUT RECEIPT",
                              font=('Arial', 18, 'bold'),
                              fg='white', bg='#2d2d2d')
        title_label.pack(pady=20)
        
        store_label = tk.Label(self.root,
                              text="Subham's Fresh Store",
                              font=('Arial', 12),
                              fg='lightgray', bg='#2d2d2d')
        store_label.pack()
        
        date_label = tk.Label(self.root,
                             text=f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
                             font=('Arial', 10),
                             fg='lightgray', bg='#2d2d2d')
        date_label.pack(pady=(0, 20))
        
        # Items header
        header_label = tk.Label(self.root,
                               text="Items Purchased:",
                               font=('Arial', 14, 'bold'),
                               fg='lightblue', bg='#2d2d2d')
        header_label.pack(pady=10)
        
        # Items list
        total_amount = 0
        for item in self.cart_items:
            item_text = f"{item['name']} - {item['quantity']} kg × ₹{item['price_per_kg']} = ₹{item['total']}"
            item_label = tk.Label(self.root,
                                 text=item_text,
                                 font=('Arial', 11),
                                 fg='white', bg='#2d2d2d')
            item_label.pack()
            total_amount += item['total']
        
        # Total
        total_label = tk.Label(self.root,
                              text=f"TOTAL AMOUNT: ₹{total_amount}",
                              font=('Arial', 16, 'bold'),
                              fg='lightgreen', bg='#2d2d2d')
        total_label.pack(pady=20)
        
        # Buttons
        confirm_btn = tk.Button(self.root,
                               text="Confirm Purchase",
                               font=('Arial', 14),
                               bg='green', fg='white',
                               width=20, height=2,
                               command=self.confirm_purchase)
        confirm_btn.pack(pady=10)
        
        back_btn = tk.Button(self.root,
                            text="Back to Main Menu",
                            font=('Arial', 12),
                            bg='gray', fg='white',
                            width=20, height=1,
                            command=self.show_main_menu)
        back_btn.pack(pady=5)
        
    def confirm_purchase(self):
        """Confirm purchase and ask for another purchase"""
        self.clear_screen()
        
        # Thank you message
        thanks_label = tk.Label(self.root,
                               text="Thank you for shopping with us!",
                               font=('Arial', 16, 'bold'),
                               fg='white', bg='#2d2d2d')
        thanks_label.pack(pady=30)
        
        success_label = tk.Label(self.root,
                                text="Your purchase has been confirmed.",
                                font=('Arial', 12),
                                fg='lightgreen', bg='#2d2d2d')
        success_label.pack(pady=10)
        
        # Ask for another purchase
        question_label = tk.Label(self.root,
                                 text="Do you want to make another purchase?",
                                 font=('Arial', 14),
                                 fg='white', bg='#2d2d2d')
        question_label.pack(pady=30)
        
        # Yes button
        yes_btn = tk.Button(self.root,
                           text="1 - Yes, shop again",
                           font=('Arial', 12),
                           bg='green', fg='white',
                           width=20, height=2,
                           command=self.start_new_shopping)
        yes_btn.pack(pady=10)
        
        # No button
        no_btn = tk.Button(self.root,
                          text="0 - No, exit store",
                          font=('Arial', 12),
                          bg='red', fg='white',
                          width=20, height=2,
                          command=self.exit_store)
        no_btn.pack(pady=10)
        
    def start_new_shopping(self):
        """Start new shopping session"""
        self.cart_items.clear()  # Clear cart
        messagebox.showinfo("New Shopping Session", "Your cart has been refreshed. Kindly shop again!")
        self.show_main_menu()
        
    def exit_store(self):
        """Exit the store"""
        messagebox.showinfo("Thank You!", "Thank you for shopping at Subham's Fresh Store.\nHave a nice day!!!")
        self.root.quit()
        
    def run(self):
        """Start the application"""
        self.root.mainloop()

# Create and run the application
if __name__ == "__main__":
    app = SimpleGroceryStoreGUI()
    app.run()