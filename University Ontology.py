import graphviz

# Create a Graphviz graph
g = graphviz.Graph()

# Add nodes to the graph
g.node('student', shape='diamond', label='étudiant', color='blue')
g.node('professor', shape='diamond', label='professeur', color='red')
g.node('course', shape='diamond', label='cours')
g.node('department', shape='diamond', label='département')
g.node('university', shape='diamond', label='université')
g.node('john_name', shape='circle', label='John', color='green')
g.node('john_age', shape='circle', label='22', color='green')
g.node('john_major', shape='circle', label='informatique', color='green')

# Add edges to the graph
g.edge('student', 'course', label='suit cours')
g.edge('professor', 'course', label='enseigne cours')
g.edge('course', 'department', label='est offert par département')
g.edge('department', 'university', label='appartient à université')

# Add subclasses
with g.subgraph(name='cluster_student') as c:
    c.attr(style='filled', color='lightgrey')
    c.node_attr.update(style='filled', color='white')
    c.attr(label='étudiant')

    c.node('student_undergrad', label='étudiant de premier cycle')
    c.node('student_graduate', label='étudiant de deuxième cycle')
    c.node('student_phd', label='étudiant de troisième cycle')
    c.edge('student_undergrad', 'student', label='est une sous-classe de')
    c.edge('student_graduate', 'student', label='est une sous-classe de')
    c.edge('student_phd', 'student', label='est une sous-classe de')



# Add properties and property values
g.node('student_name', label='nom', _attributes={'style': 'dotted'})
g.node('student_age', label='âge', _attributes={'style': 'dotted'})
g.node('student_major', label='domaine de spécialisation', _attributes={'style': 'dotted'})
g.edge('student', 'student_name', label='a pour propriété', style='solid')
g.edge('student', 'student_age', label='a pour propriété', style='solid')
g.edge('student', 'student_major', label='a pour propriété', style='solid')
g.edge('john_name', 'student_name', label='est une valeur de propriété de', style='solid')
g.edge('john_age', 'student_age', label='est une valeur de propriété de', style='solid')
g.edge('john_major', 'student_major', label='est une valeur de propriété de', style='solid')

#Add annotations
g.node('john_annotation', label='John est un étudiant de premier cycle en informatique', _attributes={'style': 'dotted'})
g.edge('john_annotation', 'john_name', label='annoté sur', style='dotted')

# Render the graph as a PNG image
g.render(format='png', filename='university_ontology.png')