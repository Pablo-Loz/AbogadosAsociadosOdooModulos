{
    'name':'Expedientes',
    'author':'Pablo Lozano Aunion, Luis Roberto Cordero Martinez, Cristian Francisco Navarro Pertegal.',
    'description':'Modulo de Expedientes permite la gestion de ellos',
    'category': 'AbogadosAsociados',
    'summary':"Estamos ante el modulo mas grande y complejo de todo nuestro trabajo donde se juntan varias relaciones, entre Abogados, "
              "diferentes Documentos, Tramites, Clientes",

    'application': True,
    'installable': True,
    'data': [
    'views/festivo_views.xml',
    'views/expediente.xml',
    'views/tramites_views.xml',
    'views/views.xml',
    'security.xml',
    'sequence.xml'
    ],
    'icon': '/expedientes/static/description/icon.png',
    'depends': ['base', 'Clientes','Abogados','Juzgados','Aseguradoras']
}