import math

def calculate_values(inputs):
    result = {}
    
    try:
        reactor = inputs["reactor"]
        CA0 = float(inputs["CA0"])
        k = float(inputs["k"])
        X = float(inputs["X"])
    except (KeyError, ValueError, TypeError):
        result["text_result"] = "❌ Invalid or missing input values."
        result["value"] = None
        return result

    if reactor in ["CSTR", "PFR"]:
        try:
            v0 = float(inputs["v0"])
        except (KeyError, ValueError, TypeError):
            result["text_result"] = "❌ Invalid or missing v0 for flow reactors."
            result["value"] = None
            return result

    if reactor == "CSTR":
        try:
            denominator = k * CA0 * (1 - X)
            if denominator == 0:
                raise ZeroDivisionError
            V = v0 * (X / denominator)
            result["text_result"] = f"📦 **CSTR Volume Required:** {V:.2f} L"
            result["value"] = V
        except ZeroDivisionError:
            result["text_result"] = "❌ Division by zero in CSTR calculation."
            result["value"] = None

    elif reactor == "PFR":
        try:
            denominator = (1 - X)
            if denominator == 0:
                raise ZeroDivisionError
            V = (v0 / (k * CA0)) * (X / denominator)
            result["text_result"] = f"📦 **PFR Volume Required:** {V:.2f} L"
            result["value"] = V
        except ZeroDivisionError:
            result["text_result"] = "❌ Division by zero in PFR calculation."
            result["value"] = None

    elif reactor == "Batch":
        try:
            if X >= 1 or X <= 0:
                raise ValueError
            t = (1 / (k * CA0)) * math.log(1 / (1 - X))
            result["text_result"] = f"⏱️ **Batch Reactor Time Required:** {t:.2f} min"
            result["value"] = t
        except (ZeroDivisionError, ValueError):
            result["text_result"] = "❌ Invalid input values for Batch reactor (X must be between 0 and 1)."
            result["value"] = None
    else:
        result["text_result"] = "❌ Unknown reactor type selected."
        result["value"] = None

    return result
