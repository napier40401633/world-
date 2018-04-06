from flask import Flask, render_template, request
import json

w = json.load(open("worldl.json"))
for c in w:
	c['tld'] = c['tld'][1:]
page_size = 20
page_number =10
app = Flask(__name__)

@app.route('/')
def mainPage():
	return render_template('index.html',
		w = w[0:page_size],page_number=page_number,page_size=page_size)

@app.route('/begin/<b>')
def beginPage(b):
	bn = int(b)
	return render_template('index.html',
		w = w[bn:bn+page_size],
		page_number = bn,
		page_size = page_size
		)

@app.route('/continent/<a>')
def continentPage(a):
	cl = [c for c in w if c['continent']==a]
	return render_template(
		'continent.html',
		length_of_cl = len(cl),
		cl = cl,
		a = a
		)

@app.route('/country/<i>')
def countryPage(i):
	return render_template(
		'country.html',
		c = w[int(i)])

@app.route('/countryByName/<n>')
def countryByNamePage(n):
	c = None
	for x in w:
		if x['name'] == n:
			c = x
	return render_template(
		'country.html',
		c = c)

@app.route('/editCountryByName/<n>')
def editCountryByNamePage(n):
		c = None
		for x in w:
				if x['name'] == n:
						c = x
		return render_template('countryedit.html',c=c)

@app.route('/updateCountryByName')
def updateCountryByNamePage():
		n = request.args.get('name')
		c = None
		for x in w:
				if x['name'] == n:
						c = x
		c['capital'] = request.args.get('capital')
		c['continent'] = request.args.get('continent')
		c['tld'] = request.args.get('tld')
		c['area'] = int(request.args.get('area'))
		c['population']  = int(request.args.get('population'))
		c['gdp']  = float(request.args.get('gdp'))
		return render_template(
					'country.html',
					c = c)

@app.route('/delete/<n>')
def deleteCountry(n):
        i = 0
        for c in w:
                if c['name'] == n:
                        break
                i = i+1
        del w[i]
        return render_template('index.html',
                w = w[0:page_size],
                page_number = 0,
                page_size = page_size
                )
@app.route('/createcountry')
def createCountryByName():
	return render_template('createcountry.html', c=c)

'''@app.route('/addcountrybyname')
def addcountryByNamePage():
	n = request.args.get('country')
	c = {}
	c['name'] = n
	c['capital'] = request.args.get('capital')
	c['continent'] = request.args.get('continent')
	c['area'] = int(request.args.get('area'))
	c['gdp']  = float(request.args.get('gdp'))
	c['tld']  = request.args.get('tld')
	c['population']  = int(request.args.get('population'))
	w.append(c)
	w.sort(key = lambda c: c['name'])
	return render_template(
		'country.html',
		c = c)'''

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5033, debug=True)






