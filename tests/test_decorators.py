from decorators.decorators import decorator, id_generator


def test_decorator(capsys):

    @decorator
    def multiply(a, b):
        return a * b

    assert multiply(2, 2) == 4
    captured = capsys.readouterr()
    output_lines = captured.out.strip().split("\n")
    assert output_lines[0] == "Start function"
    assert output_lines[1] == "Finish function"


def test_id_generator():
    greeting_func = id_generator("USER")
    assert greeting_func() == "USER-001"
    assert greeting_func() == "USER-002"
    assert greeting_func() == "USER-003"
