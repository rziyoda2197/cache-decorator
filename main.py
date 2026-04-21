import os
import jinja2

class ReportGenerator:
    def __init__(self, template_dir, output_dir):
        self.template_dir = template_dir
        self.output_dir = output_dir
        self.jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(self.template_dir))

    def generate_report(self, data, template_name):
        template = self.jinja_env.get_template(template_name)
        output_file = os.path.join(self.output_dir, f"{template_name}.txt")
        with open(output_file, "w") as f:
            f.write(template.render(data))

# Misol foydalanish:
if __name__ == "__main__":
    template_dir = "templates"
    output_dir = "output"
    report_generator = ReportGenerator(template_dir, output_dir)

    data = {
        "name": "John Doe",
        "age": 30,
        "city": "New York"
    }

    report_generator.generate_report(data, "report_template")
```

```bash
# templates/reports.j2
Name: {{ name }}
Age: {{ age }}
City: {{ city }}
```

```bash
# templates/report_template.j2
<!DOCTYPE html>
<html>
<head>
    <title>Report</title>
</head>
<body>
    <h1>Report</h1>
    <p>Name: {{ name }}</p>
    <p>Age: {{ age }}</p>
    <p>City: {{ city }}</p>
</body>
</html>
