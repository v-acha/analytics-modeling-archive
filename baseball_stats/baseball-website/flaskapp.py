from flask import Flask, render_template, request

app = Flask(__name__)

@app.before_request
def before_request():
    # Set the base URL depending on the environment
    if '127.0.0.1' in request.host:
        app.config['BASE_URL'] = '/'
    else:
        app.config['BASE_URL'] = '/baseball-viz/'

# Route for the Home Page
@app.route('/')
def home():
    base_url = app.config['BASE_URL']
    return render_template('index.html', base_url=base_url)

@app.route('/run-expectancy')
def run_expectancy():
    base_url = app.config['BASE_URL']
    return render_template('run-expectancy.html', base_url=base_url)

@app.route('/offensive-stats')
def offensive_stats():
    base_url = app.config['BASE_URL']
    return render_template('offensive-stats.html', base_url=base_url)

@app.route('/pitching-stats')
def pitching_stats():
    base_url = app.config['BASE_URL']
    return render_template('pitching-stats.html', base_url=base_url)

@app.route('/fastball-velocity')
def fastball_velocity():
    base_url = app.config['BASE_URL']
    return render_template('fastball-velocity.html', base_url=base_url)

@app.route('/batting_average')
def strikeouts_runs():
    base_url = app.config['BASE_URL']
    return render_template('batting_average.html', base_url=base_url)

@app.route('/payroll-wins')
def payroll_wins():
    base_url = app.config['BASE_URL']
    return render_template('payroll-wins.html', base_url=base_url)

@app.route('/knowledge-base')
def knowledge_base():
    base_url = app.config['BASE_URL']
    return render_template('knowledge-base.html', base_url=base_url)

@app.route('/contact')
def contact():
    base_url = app.config['BASE_URL']
    return render_template('contact.html', base_url=base_url)

# Embed images
@app.route('/embed/home_awaydistr')
def home_awaydistr():
    base_url = app.config['BASE_URL']
    return render_template('embed/home_awaydistr.html', base_url=base_url)

@app.route('/embed/home_awayscatter')
def home_awayscatter():
    base_url = app.config['BASE_URL']
    return render_template('embed/home_awayscatter.html', base_url=base_url)

@app.route('/embed/tweet_heatmap')
def tweet_heatmap():
    base_url = app.config['BASE_URL']
    return render_template('embed/tweet_heatmap.html', base_url=base_url)

@app.route('/embed/interactive_trend_charts')
def int_trendchart():
    base_url = app.config['BASE_URL']
    return render_template('embed/interactive_trend_charts.html', base_url=base_url)

@app.route('/embed/payroll_vs_winning_chart')
def payroll_winning():
    base_url = app.config['BASE_URL']
    return render_template('embed/payroll_vs_winning_chart.html', base_url=base_url)

@app.route('/embed/trend_charts')
def trend():
    base_url = app.config['BASE_URL']
    return render_template('embed/trend_charts.html', base_url=base_url)

if __name__ == "__main__":
    app.run(debug=True)
