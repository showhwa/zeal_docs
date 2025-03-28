import requests
import time
import os


languages = [
    "ActionScript", "Akka", "Angular", "AngularJS", "Ansible", "Apache_HTTP_Server", 
    "Appcelerator_Titanium", "AppleScript", "Arduino", "AWS_JavaScript", "BackboneJS", 
    "Bash", "Boost", "Bootstrap_2", "Bootstrap_3", "Bootstrap_4", "Bootstrap_5", 
    "Bourbon", "C", "C++", "CakePHP", "Cappuccino", "Chai", "Chef", "Clojure", 
    "CMake", "Cocos2D", "Cocos2D-X", "Cocos3D", "CodeIgniter", "CoffeeScript", 
    "ColdFusion", "Common_Lisp", "Compass", "Cordova", "Corona", "CouchDB", "Craft",
    "CSS", "D3JS", "Dart", "Django", "Docker", "Doctrine_ORM", "Dojo", "Drupal_10",
    "Drupal_7", "Drupal_8", "Drupal_9", "ElasticSearch", "Elixir", "Emacs_Lisp",
    "EmberJS", "Emmet", "Erlang", "Express", "ExpressionEngine", "ExtJS", "Flask", 
    "Font_Awesome", "Foundation", "GLib", "Go", "Gradle_DSL", "Gradle_Java_API", 
    "Gradle_User_Guide", "Grails", "Groovy", "Groovy_JDK", "Grunt", "Gulp", "Haml", 
    "Handlebars", "Haskell", "HTML", "HTTP", "Ionic", "Jasmine", "Java", 
    "JavaScript", "Jekyll", "Jinja", "Joomla", "jQuery", "jQuery_Mobile", "jQuery_UI", 
    "Julia", "KnockoutJS", "Kobold2D", "Laravel", "LaTeX", "Less", "Lo-Dash", 
    "Lua_5.1", "Lua_5.2", "Lua_5.3", "Lua_5.4", "MarionetteJS", "Markdown", 
    "Matplotlib", "Meteor", "Mocha", "MomentJS", "MongoDB", "Mongoose", "MooTools",
    "MySQL", "Neat", "Nginx", "NodeJS", "NumPy", "OCaml", "OpenCV", "OpenGL_2",
    "OpenGL_3", "OpenGL_4", "Pandas", "Perl", "Phalcon", "PhoneGap", "PHP",
    "PHPUnit", "Play_Java", "Play_Scala", "Polymer.dart", "PostgreSQL", "Processing", 
    "PrototypeJS", "Pug", "Puppet", "Python_2", "Python_3", "Qt_4", "Qt_5", "Qt_6", 
    "R", "Racket", "React", "Redis", "RequireJS", "Ruby", "Ruby_2", "Ruby_3", 
    "Ruby_on_Rails_3", "Ruby_on_Rails_4", "Ruby_on_Rails_5", "Ruby_on_Rails_6", 
    "Ruby_on_Rails_7", "RubyMotion", "Rust", "SailsJS", "SaltStack", "Sass", "Scala", 
    "SciPy", "Semantic_UI", "Sencha_Touch", "Sinon", "Smarty", "Sparrow", 
    "Spring_Framework", "SQLAlchemy", "SQLite", "Statamic", "Stylus", "Susy", "SVG", 
    "Swift", "Symfony", "Tcl", "Tornado", "Twig", "Twisted", "TypeScript", "TYPO3", 
    "UnderscoreJS", "Unity_3D", "Vagrant", "Vim", "VMware_vSphere", "VueJS", 
    "WordPress", "Xojo", "XSLT", "Yii", "YUI", "Zend_Framework_1", "Zend_Framework_2", 
    "Zend_Framework_3", "ZeptoJS"
]

print(len(languages))

# https://www.kapeli.com/feeds/Go.tgz
# https://go.zealdocs.org/d/com.kapeli/Go/latest
error_log = ''

for language in languages:
    time.sleep(1)
    url = f"https://go.zealdocs.org/d/com.kapeli/{language}/latest"
    # url = f"https://www.kapeli.com/feeds/{language}.tgz"
    code = requests.head(url).status_code
    if code == 404:
        print(language + "404\n")
        error_log += f'{project}: 404\n'
    else:
        # pass
        # print(language + ": " + "OK\n")
        if not os.path.isdir("docs"):
            os.mkdir("docs")
        download = requests.get(url)
        download.raise_for_status()
        with open(f"docs/{language}.tgz", 'wb') as file:
            file.write(download.content)
        print(f"{language}已下载到当前目录: docs/{language}.tgz")

if not error_log:
    if os.path.isfile("error_log.txt"):
        os.remove("error_log.txt")
else:
    with open("error_log.txt", "w", encoding="utf-8") as file:
        file.write(error_log)