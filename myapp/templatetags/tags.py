from django import template

register = template.Library()

# So that I can use this filter to add attributes to my elements in templates such as:
# {{ form.email|htmlattributes:"class : something, id: openid_identifier" }}
# So my input email now have a class=something and id=openid_identifier
def htmlattributes(value, arg):
    attrs = value.field.widget.attrs

    data = arg.replace(' ', '')
    kvs = data.split(',')

    for string in kvs:
        kv = string.split(':')
        attrs[kv[0]] = kv[1]

    rendered = str(value)
    return rendered

register.filter('htmlattributes', htmlattributes)

# I use this for debugging objects into the templates
def debug_object_dump(var):
    return vars(var)

register.filter('debug_object_dump', debug_object_dump)