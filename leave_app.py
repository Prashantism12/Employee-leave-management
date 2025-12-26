class Employee:
    def __init__(self, emp_id, name, department, total_leaves, used_leaves):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.total_leaves = total_leaves
        self.used_leaves = used_leaves

    def remaining_leaves(self):
        return self.total_leaves - self.used_leaves

    def leave_status(self):
        remaining = self.remaining_leaves()
        if remaining >= 10:
            return "Sufficient Leave"
        elif 1 <= remaining < 10:
            return "Low Leave Balance"
        else:
            return "No Leave Available"

    def display(self):
        print("\n--- Employee Leave Report ---")
        print(f"Employee ID   : {self.emp_id}")
        print(f"Name          : {self.name}")
        print(f"Department    : {self.department}")
        print(f"Remaining     : {self.remaining_leaves()}")
        print(f"Status        : {self.leave_status()}")


def main():
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    dept = input("Enter Department: ")
    total = int(input("Total Leaves Allocated: "))
    used = int(input("Leaves Used: "))

    emp = Employee(emp_id, name, dept, total, used)
    emp.display()


if __name__ == "__main__":
    main()