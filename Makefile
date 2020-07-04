all:
	-rm static/js/flosstudio.js
	echo 'database = ' > static/js/flosstudio.js
	wget https://raw.githubusercontent.com/flosstudio/schema/master/flosstudio.schema.yaml
	yq . flosstudio.schema.yaml >> static/js/flosstudio.js
	cat static/js/_flosstudio.js >> static/js/flosstudio.js
	rm flosstudio.schema.yaml
