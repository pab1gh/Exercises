
def test_solution(monkeypatch):
    ret_val1= None

    def g(num1):
       nonlocal ret_val1
       ret_val1=num1

    monkeypatch.setattr('builtins.print',g)

    import solution
    assert type(solution.x) == int and type(solution.y) == int
    assert solution.result == False

