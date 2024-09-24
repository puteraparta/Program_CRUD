# Importing tabulate to format table
from tabulate import tabulate

# Inventory data for various Spare Parts with Collection Data Type Dictionary in List
data_part=[{                                
            'part_number':'1211371',
            'part_name':'Seal',
            'brand':'Caterpillar',
            'part_quantity':10,
            'piece_price':30000,
            'stock_status':'In Stock'
            },
            {
            'part_number':'1141267',
            'part_name':'Valve Group',
            'brand':'Caterpillar',
            'part_quantity':2,
            'piece_price':3000000,
            'stock_status':'In Stock'
            },
            {
            'part_number':'0716110090',
            'part_name':'Ring Piston',
            'brand':'Komatsu',
            'part_quantity':3,
            'piece_price':120000,
            'stock_status':'In Stock'
            },
            {
            'part_number':'14Y5011421',
            'part_name':'Bushing',
            'brand':'Komatsu',
            'part_quantity':4,
            'piece_price':220000,
            'stock_status':'In Stock'
            },
            {
            'part_number':'23A1515910',
            'part_name':'Gasket',
            'brand':'Komatsu',
            'part_quantity':0,
            'piece_price':380000,
            'stock_status':'Out of Stock'
            },
            {
            'part_number':'0000146756',
            'part_name':'Seal Ring',
            'brand':'Renault',
            'part_quantity':0,
            'piece_price':70000,
            'stock_status':'Out of Stock'
            },
            ]

# Placeholder lists for various operations
preview_add_stock=[]         # Placeholder for previewing additions to stock
preview_check_level = []     # Placeholder for previewing checking stock levels
preview_delete_stock = []    # Placeholder for previewing deletions from stock
preview_update_quantity = [] # Placeholder for previewing quantity updates
preview_order = []           # Placeholder for previewing orders
view_order = []              # Placeholder for viewing orders
filter_view_order = []       # Placeholder for filtering and viewing orders

# DISPLAY FUNCTION
# Function to view stock data for parts
def view_stock_part(data_part):                 
    print("\nStock Data")                       # Print a header for the stock data
    empty_list=[]                               # Initialize an empty list to store formatted data rows
    for i in data_part:                         # Iterate through each part dictionary in data_part

        # Extract relevant information from the part dictionary and append as a list
        empty_list.append([i['part_number'],i['part_name'],i['brand'],i['part_quantity'],i['piece_price'],i['stock_status']])

    # Print the formatted data using tabulate with specific formatting options
    print(tabulate(empty_list, headers=['Part_Number', 'Part_Name', 'Brand', 'Part_Qty_(Pcs)', 'Piece_Price_(Rp)', 'Stock_Status'], tablefmt='mixed_grid', numalign='left', stralign='center')) 

# Function to display current stock data for parts
def show_stock_part(data_part):
    print("\nSpare Parts Stock Report")
    empty_list=[]
    for i in data_part:
        empty_list.append([i['part_number'],i['part_name'],i['brand'],i['part_quantity'],i['piece_price'], i['stock_status']])
    print(tabulate(empty_list, headers=['Part_Number', 'Part_Name', 'Brand', 'Part_Qty_(Pcs)', 'Piece_Price_(Rp)', 'Stock_Status'], tablefmt='fancy_grid', numalign='center', stralign='center'))
    print("Signature,\n\n\n\n(Staff Warehouse)")

# Function to preview new part stock additions
def show_add_stock(preview_add_stock):
    print("\nNew Part Stock Preview")
    empty_list=[]
    for i in preview_add_stock:
        empty_list.append([i['part_number'],i['part_name'],i['brand'],i['part_quantity'],i['piece_price']])
    print(tabulate(empty_list, headers=['Part_Number', 'Part_Name', 'Brand', 'Part_Qty_(Pcs)', 'Piece_Price_(Rp)'], tablefmt='pretty', numalign='center', stralign='center'))

# Function to display all stock levels
def show_all_stock_level(data_part):
    print("\nAll Stock Level")
    empty_list=[]
    for i in data_part:
        empty_list.append([i['part_number'],i['part_name'],i['brand'],i['part_quantity']])
    print(tabulate(empty_list, headers=['Part_Number', 'Part_Name', 'Brand', 'Part_Qty_(Pcs)'], tablefmt='mixed_grid', numalign='center', stralign='center'))

# Function to display the particular part quantity
def show_stock_level(preview_check_level):
    print("\nCheck Level Stock")
    empty_list=[]
    for i in preview_check_level:
        empty_list.append([i['part_number'],i['part_name'],i['brand'],i['part_quantity']])
    print(tabulate(empty_list, headers=['Part_Number', 'Part_Name', 'Brand', 'Part_Qty_(Pcs)'], tablefmt='pretty', numalign='center', stralign='center'))

# Function to preview updated quantities
def show_update_quantity(preview_update_quantity):
    print("\nUpdate Quantity Preview")
    empty_list=[]
    for i in preview_update_quantity:
        empty_list.append([i['part_number'],i['part_name'],i['brand'],i['part_quantity']])
    print(tabulate(empty_list, headers=['Part_Number', 'Part_Name', 'Brand', 'Part_Qty_(Pcs)'], tablefmt='pretty', numalign='center', stralign='center'))

# Function to preview stock deletions
def show_delete_stock(preview_delete_stock):
    print("\nDelete Stock Preview")
    empty_list=[]
    for i in preview_delete_stock:
        empty_list.append([i['part_number'],i['part_name'],i['brand'],i['part_quantity'],i['piece_price'],i['stock_status']])
    print(tabulate(empty_list, headers=['Part_Number', 'Part_Name', 'Brand', 'Part_Qty_(Pcs)', 'Piece_Price_(Rp)','Stock_Status'], tablefmt='pretty', numalign='center', stralign='center'))

# Function to preview processing orders
def show_process_order(preview_order):
    print("\nOrder Stock Preview")
    empty_list=[]
    for i in preview_order:
        empty_list.append([i['order_id'],i['part_number'],i['part_name'],i['brand'],i['part_quantity'],i['piece_price']])
    print(tabulate(empty_list, headers=['Order_ID','Part_Number', 'Part_Name', 'Brand', 'Part_Qty_(Pcs)', 'Piece_Price_(Rp)'], tablefmt='pretty', numalign='center', stralign='center'))

# Function to view order parts list
def view_order_part(view_order):
    print("\nOrder Stock List")
    empty_list=[]
    for i in view_order:
        empty_list.append([i['order_id'],i['part_number'],i['part_name'],i['brand'],i['part_quantity'],i['piece_price']])
    print(tabulate(empty_list, headers=['Order_ID','Part_Number', 'Part_Name', 'Brand', 'Part_Qty_(Pcs)', 'Piece_Price_(Rp)'], tablefmt='simple_grid', numalign='center', stralign='center'))

# Function to filter order stock by order ID
def filter_order_stock(filter_view_order):
    print("\nFiltered Order List by Order ID")
    empty_list=[]
    for i in filter_view_order:
        empty_list.append([i['order_id'],i['part_number'],i['part_name'],i['brand'],i['part_quantity'],i['piece_price']])
    print(tabulate(empty_list, headers=['Order_ID','Part_Number', 'Part_Name', 'Brand', 'Part_Qty_(Pcs)', 'Piece_Price_(Rp)'], tablefmt='pretty', numalign='center', stralign='center'))

# Function to show sort Data Part by Quantity in descending order
def show_sort_part_desc():
    if len(data_part)>0:
        print("\nSpare Parts Stock Report by Quantity")
        
        sort_report_descending(data_part)
        
        empty_list = []
        for part in data_part:
            empty_list.append([part['part_number'],part['part_name'],part['brand'],part['part_quantity'],part['piece_price'],part['stock_status']
            ])
        
        print(tabulate(empty_list, headers=['Part_Number', 'Part_Name', 'Brand', 'Part_Qty_(Pcs)', 'Piece_Price_(Rp)', 'Stock_Status'], tablefmt='fancy_grid', numalign='center', stralign='center'))
        print("Signature,\n\n\n\n(Staff Warehouse)")
    else:
        print('''\n\t\t\t\t\tData Part is Empty.\n\t\t\t\t\tPlease Add New Part.''')

# Function to show sort Data Part by Quantity in ascending order
def show_sort_part_asce():
    if len(data_part)>0:
        print("\nSpare Parts Stock Report by Quantity")
        
        sort_report_ascending(data_part)
        
        empty_list = []
        for part in data_part:
            empty_list.append([part['part_number'],part['part_name'],part['brand'],part['part_quantity'],part['piece_price'],part['stock_status']
            ])
        
        print(tabulate(empty_list, headers=['Part_Number', 'Part_Name', 'Brand', 'Part_Qty_(Pcs)', 'Piece_Price_(Rp)', 'Stock_Status'], tablefmt='fancy_grid', numalign='center', stralign='center'))
        print("Signature,\n\n\n\n(Staff Warehouse)")
    else:
        print('''\n\t\t\t\t\tData Part is Empty.\n\t\t\t\t\tPlease Add New Part.''')

# MAIN MENU AND SUB MENU FUNCTION
# OPTION MAIN MENU:1
def stock_management_menu(sub_menu):
    while True:
        sub_menu = input('''
                            Please select the Stock Management Menu:
                            1. Add New Spare Part
                            2. Update Spare Part Quantity
                            3. Check Part Stock Level
                            4. Delete Spare Part
                            5. Back To Main Menu
                            Enter the MENU number you want to run (1-5): ''')

        if (sub_menu == '1'):
            add_new_part()
        elif (sub_menu == '2'):
            update_stock_quantity()
        elif (sub_menu == '3'):
            check_stock_part_menu(sub_menu)
        elif (sub_menu == '4'):
            delete_part_stock_menu(sub_menu)
        elif (sub_menu == '5'):
            break
        else:
            print('''
                    Invalid selection. Please enter the correct MENU number (1-5).''')

def add_new_part():
    while True:
        while True:
            while True: 
                part_number = input("\nEnter Part Number: ")
                
                part_number_str=''
                for i in range(len(part_number.split())):
                    part_number_str=part_number_str+part_number.split()[i]
                
                is_valid = True
                for i in part_number_str:
                    if not ('0' <= i <= '9' or 'A' <= i <= 'Z' or 'a' <= i <= 'z'):
                        is_valid = False
                        break
                
                if part_number_str != ''and is_valid:    
                    part_number=part_number_str
                    break
                elif not is_valid:
                    print("Input invalid. Please input only alphabetic characters and number.")
                else:
                    print('Empty Part Number Input')

            for i in range(len(data_part)):
                if data_part[i]['part_number'] == part_number.upper():
                    print(f'''Part number '{data_part[i]["part_number"]}' with name '{data_part[i]["part_name"]}' and brand '{data_part[i]["brand"]}' already exist.''')
                    break

            else:
                break
            
        while True:
            part_name = input(f"Enter Part Name for '{part_number.upper()}': ")
            if part_name != '':
                break
            print('Empty Part Name Input')
        
        while True:
            brand = input(f"Enter Brand for {part_name.title()} with '{part_number.upper()}': ")
            if brand != '':
                break
            print('Empty Brand Input')
            
        while True:
            part_quantity=(input(f'Enter Part Quantity for {part_name.title()} with {part_number.upper()}: '))
            if part_quantity.isdigit() and int(part_quantity)>0:
                part_quantity = int(part_quantity)
                break
            else:
                print("Part Quantity must an interger positive number. Please try again.")
        
        while True:
            piece_price=(input(f'Enter Piece Price for {part_name.title()} with {part_number.upper()}: '))
            if piece_price.isdigit() and int(piece_price)>0:
                piece_price = int(piece_price)
                break
            else:
                print("Piece Price must an integer positive number. Please try again.")

        data_part[i]['part_quantity'] = part_quantity
        if part_quantity == 0:
            stock_status= 'Out of Stock'
        else:
            stock_status= 'In Stock'      

        preview_add_stock.append(
                {
                    'part_number':part_number.upper(),
                    'part_name':part_name.title(), 
                    'brand':brand.title(), 
                    'part_quantity':part_quantity,
                    'piece_price':piece_price,
                    'stock_status':stock_status.title()
                }
            )
        
        show_add_stock(preview_add_stock)
        while True:    
            checker=input('Are you sure you want to save this new Part? (yes/no):')
            if checker.lower()!='yes' and checker.lower()!='no':
                print("Input invalid. Please try again.")
            else:
                break
        
        if checker.lower() == 'no':
            preview_add_stock.pop()
            print("Add New Part is Canceled")
            break
        else:
            preview_add_stock.pop()           
            data_part.append(
                        {
                            'part_number':part_number.upper(), 
                            'part_name':part_name.capitalize(), 
                            'brand':brand.capitalize(), 
                            'part_quantity':part_quantity,
                            'piece_price':piece_price,
                            'stock_status':stock_status.title()
                        }
                    )
            print('Part has succesfully saved')
            break

def update_stock_quantity():
    if len(data_part)>0:
        while True:
            while True:
                part_number = input('\nEnter the Part Number you wish to update (cancel to exit ): ')
                if part_number != '':
                    break
                else:
                    print("Invalid input. Please enter a valid part number.")
            
            if part_number.lower() == 'cancel':
                break

            for i in range(len(data_part)):
                if data_part[i]['part_number'] == part_number.upper():
                    break
            else:
                print(f"Part Number '{part_number.upper()}' does not exist.")
                continue
            
            index = 0
            for j in range(len(data_part)):
                if data_part[j]['part_number'] == part_number.upper():
                    index = j
                    break

            while True:
                new_part_quantity = input(f"Enter new quantity for {data_part[index]['part_number']}: ")
                if new_part_quantity.isdigit() and int(new_part_quantity) >= 0:
                    new_part_quantity = int(new_part_quantity)
                    break
                else:
                    print("Invalid input. Please enter a valid integer.")
            
            preview_update_quantity.append({
                'part_number': data_part[index]['part_number'],
                'part_name': data_part[index]['part_name'],
                'brand': data_part[index]['brand'],
                'part_quantity': new_part_quantity,
                'piece_price': data_part[index]['piece_price'],
            })
            show_update_quantity(preview_update_quantity)

            while True:    
                checker=input(f"Do you want to update Part Quantity '{part_number}'? (yes/no):")
                if checker.lower()!='yes' and checker.lower()!='no':
                    print("Input invalid. Please try again")
                else:
                    break
            
            if checker.lower() != 'yes':
                preview_update_quantity.pop()
                print("You did not update changes")
                break
            else:
                data_part[index]['part_quantity'] = new_part_quantity
                if new_part_quantity == 0:
                    data_part[index]['stock_status'] = 'Out of Stock'
                else:
                    data_part[index]['stock_status'] = 'In Stock'
                preview_update_quantity.pop()
                print(f"The Part Quantity of Part Number '{data_part[index]['part_number']}' updated to {data_part[index]['part_quantity']}.")
                break
    else:
        while True:
            part_number = input('Enter the Part Number you wish to check: ')
            if part_number == "":
                print(f"Input is empty. Please try again")
                continue
            else:
                print(f"Data Part is Empty. Please Add New Part")
                break
                
def check_stock_part_menu(sub_menu):
    while True:
        sub_menu=input('''
                                Please select the Check Stock Level Menu:
                                1. Check All Stock Level
                                2. Check Stock Level
                                3. Back To Previous Menu
                                Enter the MENU number you want to run (1-3): ''')
        if (sub_menu=='1'):
            check_all_stock_level()
        elif (sub_menu=='2'):
            check_stock_level()    
        elif(sub_menu=='3'):
            break
        else:
            print('''
                  Invalid selection. Please enter the correct MENU number (1-3).''')

def check_all_stock_level():
    if len(data_part)>0:
        show_all_stock_level(data_part)
    else:
        print('''\n\t\t\t\t\tData Part is Empty:\n\t\t\t\t\tPlease Add New Part.''')

def check_stock_level():
    if len(data_part)>0:
        while True:
            part_number = input('\nEnter the Part Number you wish to check: ')
            if part_number == "":
                print("Input is empty. Please try again.")
                continue

            while True:    
                checker=input(f"Do you want to check Part Number '{part_number}'? (yes/no):")
                if checker.lower()!='yes' and checker.lower()!='no':
                    print("Input invalid. Please try again")
                else:
                    break
            
            if checker.lower() != 'yes':
                print("Checking stock level is Canceled")
                break
            else:
                for i in range(len(data_part)):
                    if data_part[i]['part_number'] == part_number:
                        preview_check_level.append(
                        {
                            'part_number':part_number.upper(), 
                            'part_name':data_part[i]['part_name'], 
                            'brand':data_part[i]['brand'], 
                            'part_quantity':data_part[i]['part_quantity'],
                            'piece_price':data_part[i]['piece_price'],
                            'stock_status':data_part[i]['stock_status']
                        }
                        )
                        show_stock_level(preview_check_level)
                        piece_label = 'pieces' if data_part[i]['part_quantity']> 0 else 'piece'
                        print(f"The current stock level for Part Number '{part_number}' is {data_part[i]['part_quantity']} {piece_label}.")
                        preview_check_level.pop()
                        break

                else:
                    print(f"Part Number '{part_number}' not found in inventory. Please try again.")
                    break
                
                break
    else:
        while True:
            part_number = input('Enter the Part Number you wish to check: ')
            if part_number == "":
                print("Input is empty. Please try again")
                continue
            else:
                print("Data Part is Empty. Please Add New Part")
                break

def delete_part_stock_menu(sub_menu):
    while True:
        sub_menu=input('''
                                Please select the Delete Stock Part Menu:
                                1. Delete Spare Part Stock
                                2. Delete All Stock
                                3. Back To Previous Menu
                                Enter the MENU number you want to run (1-3): ''')
        if (sub_menu=='1'):
            delete_part_stock()
        elif (sub_menu=='2'):
            delete_all_stock()    
        elif(sub_menu=='3'):
            break
        else:
            print('''
                  Invalid selection. Please enter the correct MENU number (1-3).''')

def delete_part_stock():
    if len(data_part)>0:
        while True:
            part_number = input('\nEnter the Part Number you wish to delete (cancel to exit): ').upper()
            
            if part_number == "":
                print("Input is empty. Please try again")
                continue
            elif part_number.lower()=='cancel':
                break 

            matched=False
            for i in range(len(data_part)):
                if data_part[i]['part_number'] == part_number:
                    deleted_stock = data_part[i]

                    preview_delete_stock.append(
                        {
                            'part_number': deleted_stock['part_number'], 
                            'part_name': deleted_stock['part_name'], 
                            'brand': deleted_stock['brand'], 
                            'part_quantity': deleted_stock['part_quantity'],
                            'piece_price': deleted_stock['piece_price'],
                            'stock_status': deleted_stock['stock_status']
                        }
                    )
                    
                    show_delete_stock(preview_delete_stock)
                    
                    while True:
                        checker = input(f"Are you sure you want to delete stock with Part Number '{part_number}'? (yes/no): ").lower()
                        if checker == 'yes' or checker == 'no':
                            break
                        else:
                            print("Input invalid. Please try again.")
                    
                    if checker == 'no':
                        preview_delete_stock.pop()
                        matched=True 
                        print("Delete stock data is canceled")
                        break
                    else:
                        preview_delete_stock.pop()
                        data_part.pop(i)
                        
                    print(f"Stock with Part Number '{part_number}' has been successfully DELETED.")
                    matched=True
                    break
            
            if not matched:
                print(f"Part Number '{part_number}' not found in inventory. Please try again")
                continue
            break
    else:
        while True:
            part_number = input('Enter the Part Number you wish to check: ')
            if part_number == "":
                print("Input is empty. Please try again")
                continue
            else:
                print("Data Part is Empty. Please Add New Part")
                break

def delete_all_stock():
    if len(data_part)>0:
        while True:
            checker = input('''
                                            You cannot restore the data
                                Are you sure you want to DELETE ALL STOCK DATA? (yes/no): ''')
            if checker.lower()!='yes' and checker.lower()!='no':
                print('''
                                        Input invalid. Please try again''')
            else:
                break

        if checker == 'no':
            print('''
                                            Delete all stock data is CANCELED''')
        else:
            data_part.clear()
            view_stock_part(data_part)
            print('''
                    All STOCK DATA has been successfully DELETED''')
                
    else:
        
        print('''\n\t\t\t\t\tAll Data Part HAS BEEN DELETED\n\t\t\t\t\t\tPlease Add New Spare Part.''')

# OPTION MAIN MENU: 2
def order_management_menu(sub_menu):
    while True:
        sub_menu=input('''
                            Please select the Order Inbound Management Menu:
                            1. Process Part Order Inbound
                            2. View Part Order Inbound
                            3. Back to Previous Menu
                            Enter the MENU number you want to run (1-3) : ''')
        if (sub_menu=='1'):
            process_order()
        elif (sub_menu=='2'):
            view_order_menu()
        elif(sub_menu=='3'):
            break
        else:
            print('''
                    Invalid selection. Please enter the correct MENU number (1-3).''')

def process_order():
    if len(data_part)>0:
        while True:
            while True:
                while True:
                    part_number = input(f'\nEnter Part Number to order (cancel to exit): ').upper()
                    
                    if part_number.lower()=='cancel':
                        break       # Exit the loop of inner loop if user inputs 'cancel'

                    if part_number != '':
                        matched=False
                        for i in range(len(data_part)):
                            if data_part[i]['part_number'] == part_number:
                                matched=True
                                if data_part[i]['part_quantity'] > 0:
                                    print(f"Part with Part Number '{part_number}' still In Stock. Please order Out of Stock part.")
                                    break   # Break if the part is still in stock
                                else:
                                    break   # Break if the part is out of stock
                        if not matched:
                            print(f"Part Number '{part_number}' does not exist in data part. Please try again")
                        elif data_part[i]['part_quantity'] == 0:
                            break   # Break if part is found and is out of stock
                    else:
                        print('Input is empty. Please try again')

                if part_number.lower()=='cancel':
                    break   # Exit the loop of middle loop if user inputs 'cancel'

                for i in range(len(view_order)):
                    if view_order[i]['part_number'] == part_number.upper():
                        print(f'''Part number '{view_order[i]["part_number"]}' with Order ID {view_order[i]["order_id"]} has been ordered .''')
                        break       # Inform user that the part has already been ordered
                else:
                    break       # Exit if the part has not been ordered yet
            
            if part_number.lower()=='cancel':
                break        # Exit the loop of outer loop if user inputs 'cancel' 

            while True:
                part_quantity = input(f'Enter Part Quantity for {part_number.upper()}: ')
                if part_quantity == "":
                    print("Input is empty. Please try again.")
                    continue
                if part_quantity.isdigit() and int(part_quantity) > 0:
                    part_quantity = int(part_quantity)
                    break
                else:
                    print("Part Quantity must be a positive integer number. Please try again.")
            
            index = 0
            for i in range(len(data_part)):
                if data_part[i]['part_number'] == part_number:
                    index = i
                    break           # Find the index of the part in the inventory
            
            order_id=f"ORD{part_number}{data_part[index]['brand'][:3]}"         # Generate a unique order ID

            view_order.append({
                'order_id': order_id.upper(),
                'part_number': part_number.upper(),
                'part_name': data_part[index]['part_name'],
                'brand': data_part[index]['brand'],
                'part_quantity': part_quantity,
                'piece_price': data_part[index]['piece_price'],
            })
        
            preview_order.append({
                'order_id': order_id.upper(),
                'part_number': part_number.upper(),
                'part_name': data_part[index]['part_name'],
                'brand': data_part[index]['brand'],
                'part_quantity': part_quantity,
                'piece_price': data_part[index]['piece_price'],
            })
            
            show_process_order(preview_order)

            while True:    
                checker=input('Do you want to process order? (yes/no):')
                if checker.lower()!='yes' and checker.lower()!='no':
                    print("Input invalid. Please try again.")
                else:
                    break
            
            if checker.lower() != 'yes':
                preview_order.clear()
                view_order.clear()
                print("Part Order is Canceled")
                break
            else:
                preview_order.clear()
                print("Part Order has been added to Order List")
                break    
    else:
        while True:
            part_number = input('Enter the Part Number you wish to check: ')
            if part_number == "":
                print("Input is empty. Please try again")
                continue
            else:
                print("Data Part is Empty. Please Add New Part")
                break

def view_order_menu():
    while True:
        print_sub_menu=input('''
                                Please select the View Spare Part Order Inbound Menu:
                                1. View All Available Order
                                2. Filter Order by Order ID
                                3. Back To Previous Menu
                                Enter the MENU number you want to run (1-3): ''')
        if (print_sub_menu=='1'):
            view_all_order()
        elif (print_sub_menu=='2'):
            view_order_filter()
        elif(print_sub_menu=='3'):
            break
        else:
            print('''
                        Invalid selection. Please enter the correct MENU number (1-3).''')
            
def view_all_order():
    if len(view_order)>0:
        view_order_part(view_order)
    else:
        print('''\n\t\t\t\t\tOrder Stock List:\n\t\t\t\t\tNo orders available.''')

def view_order_filter():
    if len (view_order)>0:
        while True:
            order_id = input('\nEnter the Order ID you wish to check: ')
            if order_id == "":
                print("Input is empty. Please try again.")
                continue

            while True:    
                checker=input(f"Do you want to filter by Order ID '{order_id}'? (yes/no):")
                if checker.lower()!='yes' and checker.lower()!='no':
                    print("Input invalid. Please try again")
                else:
                    break
            
            if checker.lower() != 'yes':
                print("Filter is Canceled")
                break
            else:
                for i in range(len(view_order)):
                    if view_order[i]['order_id'] == order_id:
                        filter_view_order.append(
                        {
                            'order_id':order_id.upper(),
                            'part_number':view_order[i]['part_number'], 
                            'part_name':view_order[i]['part_name'], 
                            'brand':view_order[i]['brand'], 
                            'part_quantity':view_order[i]['part_quantity'],
                            'piece_price':view_order[i]['piece_price']
                        }
                        )
                        filter_order_stock(filter_view_order)
                        print(f"Order ID {order_id}.")
                        filter_view_order.pop()
                        break

                else:
                    print(f"Order ID '{order_id}' not found in order list. Please try again.")
                    break
                
                break
    else:
        while True:
            part_number = input('\nEnter the Part Number you wish to check: ')
            if part_number == "":
                print(f"Input is empty. Please try again")
                continue
            else:
                print(f"Data Part is Empty. Please Add New Part")
                break

# OPTION MAIN MENU: 3
def report_menu(sub_menu):
    while True:
        sub_menu=input('''
                            Please select the Report Menu:
                            1. Produce Stock Report
                            2. Sort Report Stock by Quantity
                            3. Back To Previous Menu
                            Enter the MENU number you want to run (1-3): ''')
        if (sub_menu=='1'):
            show_stock_part(data_part)
        elif (sub_menu=='2'):
            sort_report_stock_menu(sub_menu) 
        elif (sub_menu=='3'): 
            break
        else:
            print('''
                  Invalid selection. Please enter the correct MENU number (1-3).''')
            
def sort_report_stock_menu(sub_menu):
    while True:
        sub_menu=input('''
                                Please select the Sort Report Stock by Quantity Menu:
                                1. Sort Report Stock Descending
                                2. Sort Report Stock Ascending
                                3. Back To Previous Menu
                                Enter the MENU number you want to run (1-3): ''')
        if (sub_menu=='1'):
            show_sort_part_desc()
        elif (sub_menu=='2'):
            show_sort_part_asce() 
        elif (sub_menu=='3'): 
            break
        else:
            print('''
                        Invalid selection. Please enter the correct MENU number (1-3).''')            

def sort_report_descending(data_part):
    for i in range(len(data_part)):
        index=i
        for j in range(i+1, len(data_part)):
            if data_part[j]['part_quantity'] < data_part[index]['part_quantity']:   # Find the index of the part with the highest quantity
                index = j
        data_part[i], data_part[index] = data_part[index], data_part[i] # Swap the position the highest quantity part at the current index    

def sort_report_ascending(data_part):
    for i in range(len(data_part)):
        index=i
        for j in range(i+1, len(data_part)):
            if data_part[j]['part_quantity'] > data_part[index]['part_quantity']:   # Find the index of the part with the lowest quantity
                index = j
        data_part[i], data_part[index] = data_part[index], data_part[i] # Swap the position the lowest quantity part at the current index

# DISPLAY MAIN MENU
def main_menu():
    while True:
        print_main_menu=input('''
======================= Heavy Equipment Spare Part Warehouse Inventory System ====================

                        Please select menu:     
                        1. Stock Management
                        2. Order Inbound Management
                        3. Report Menu
                        4. Exit Program
                        Enter the MENU number you want to run (1-4): ''')
                  
        if(print_main_menu=='1'):
            stock_management_menu(1)    
        elif(print_main_menu=='2'):
            order_management_menu(2)
        elif(print_main_menu=='3'):
            report_menu(3)
        elif(print_main_menu=='4'):
            print('\nExiting program...')
            break
        else:
            print('''
                  Invalid selection. Please enter the correct MENU number (1-4).''')

if __name__ == "__main__":            
    main_menu()