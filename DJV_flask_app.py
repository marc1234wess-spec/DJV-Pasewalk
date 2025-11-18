# Main
if __name__ == '__main__':
    import eventlet
    import eventlet.wsgi
    from werkzeug.middleware.proxy_fix import ProxyFix

    # Render erwartet den Port in der ENV
    port = int(os.environ.get("PORT", 5000))
    app.wsgi_app = ProxyFix(app.wsgi_app)
    print(f'Starte DJV auf Port {port}...')
    socketio.run(app, host='0.0.0.0', port=port)
