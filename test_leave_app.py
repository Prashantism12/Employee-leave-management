from leave_app import Employee

def test_leave_status():
    e1 = Employee("E01", "A", "HR", 20, 5)
    assert e1.leave_status() == "Sufficient Leave"

    e2 = Employee("E02", "B", "IT", 20, 15)
    assert e2.leave_status() == "Low Leave Balance"

    e3 = Employee("E03", "C", "Admin", 10, 10)
    assert e3.leave_status() == "No Leave Available"