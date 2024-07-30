
from JSONForms_Style import JSONForms_Style

def test_JSONFormsStyle():
    JSONForms_Style.parseStyleDefinitionFromJSONFile("./schema.json")
    JSONForms_Style.parseStyleDefinitionFromJSONFile("./styles.json")

    properties = JSONForms_Style.buildCompositeStyle("BUTTON")
    print(properties)

    properties = JSONForms_Style.buildCompositeStyle("BUTTON", None, "sideButtonContainer")
    print(properties)

if __name__ == "__main__":
    test_JSONFormsStyle()