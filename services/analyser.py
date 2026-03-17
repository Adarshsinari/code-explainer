import ast

def analyze_code(code: str):
    info = {
        "functions": [],
        "loops": 0,
        "imports": [],
        "classes": []
    }

    try:
        tree = ast.parse(code)

        for node in ast.walk(tree):

            if isinstance(node, ast.FunctionDef):
                info["functions"].append(node.name)

            if isinstance(node, ast.For) or isinstance(node, ast.While):
                info["loops"] += 1

            if isinstance(node, ast.Import):
                for n in node.names:
                    info["imports"].append(n.name)

            if isinstance(node, ast.ClassDef):
                info["classes"].append(node.name)

    except Exception:
        info["error"] = "Code is Invalid."

    return info