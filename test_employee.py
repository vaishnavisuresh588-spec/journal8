from employee import employee_details

def test_employee_output():
    expected_output = (
        "Employee Name : Vaishnavi\n"
        "Employee ID   : 01FE24BCA014\n"
        "Department    : BCA\n"
        "Salary        : 60000"
    
     )
    assert employee_details(
        "Vaishnavi",
        "01FE24BCA014",
        "BCA",
        60000
    ) == expected_output
