Uma forma de evitar esse problema seria passar a variavel dentro do método render_template_string(), que por padrão faz o autoescape das strings. 

```python3
@app.route('/render', methods=['POST'])
def render():
    user_input = request.form.get('input')
    template = f'Hello, {{ {user_input} }}!'
    try:
        result = render_template_string(template, user_input=user_input)
    except Exception as e:
        result = str(e)
    return render_template_string(index(), result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

```
