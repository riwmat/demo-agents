"""
Exemplo simples para demonstrar que o GitHub Copilot está funcionando.
This is a simple example to demonstrate that GitHub Copilot is working.
"""


def hello_copilot() -> str:
    """
    Função de demonstração do Copilot.
    Returns a greeting message.
    """
    return "Olá! O Copilot está funcionando! 🎉"


def add_numbers(a: float, b: float) -> float:
    """
    Soma dois números.
    Adds two numbers together.
    """
    return a + b


if __name__ == "__main__":
    print(hello_copilot())
    print(f"2 + 3 = {add_numbers(2, 3)}")
