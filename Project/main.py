from db_operations import *
from visuals import *

ops_dictionary = { 1: "birth_order_criteria",
                   2: "residence_criteria",
                   3: "stay_duration_criteria_public",
                   4: "stay_duration_criteria_private",
                   5: "wealth_quintile_criteria"}

print("Normal Delivery vs. C-Section delivery  - A Comparative analysis")
print("Criteria: \n1. Birth order \n2. Residence \n3. Duration of stay - Public Hospital \n4. Duration of stay - Private Hospital \n5. Wealth quintile")
choice = int(input("Enter choice to view graph: "))
table_data = read_table(ops_dictionary[choice])
print(table_data)
create_histogram(table_data)