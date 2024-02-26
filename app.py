from flask import Flask, request, jsonify

app=Flask(__name__)

emp_data_list=[
    {"id": 1, "name": "John Doe", "age": 28, "city": "Faketown"},
    {"id": 2, "name": "Jane Smith", "age": 35, "city": "Pseudocity"},
    {"id": 3, "name": "Bob Johnson", "age": 22, "city": "Fabricburg"},
    {"id": 4, "name": "Alice Brown", "age": 31, "city": "Imaginaria"},
    {"id": 5, "name": "Charlie Davis", "age": 29, "city": "Illusionville"},
    {"id": 6, "name": "Eva White", "age": 26, "city": "Simuland"},
    {"id": 7, "name": "Frank Black", "age": 33, "city": "Virtualburg"},
    {"id": 8, "name": "Grace Green", "age": 30, "city": "Phantasytown"},
    {"id": 9, "name": "David Grey", "age": 27, "city": "Fictionville"},
    {"id": 10, "name": "Helen Taylor", "age": 32, "city": "Dreamland"}
    ]




@app.route('/emp',methods=['GET','POST'])
def emp():
    if request.method=='GET':

        if len(emp_data_list)>0:
            return jsonify(emp_data_list),200
        else:
            return 'not found'

    if request.method=='POST':
        new_name=request.form['name']
        new_age=request.form['age']
        new_city=request.form['city']
        id=emp_data_list[-1] ['id']+1

        new_obj={'id':id,
                 'name':new_name,
                 'age':new_age,
                 'city':new_city
                 }

        emp_data_list.append(new_obj)
        return jsonify(emp_data_list),201
    
@app.route('/emps/<int:id>',methods=['GET','PUT','DELETE'])
def num_emp(id):
    if request.method=='GET':
        for emps in emp_data_list:
            if emps['id']==id:
                return jsonify(emps)
            pass
    if request.method=='PUT':
        for emps in emp_data_list:
            if emps['id']==id:
                emps['age']=request.form['age']
                emps['name']=request.form['name']
                emps['city']=request.form['city']
                updated_emp_list={
                    'id':id,
                    'age':emps['age'],
                    'city':emps['city'],
                    'name':emps['name'],

                }
                return(jsonify(updated_emp_list))
     
    if request.method=='DELETE':
        for index,emps in enumerate(emp_data_list):
            if emps['id']==id:
                emp_data_list.pop(index)
                return(jsonify(emp_data_list))

if __name__=='__main__':
    app.run()
