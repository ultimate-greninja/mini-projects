<!doctype html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <title>Viewer — Magic the Noah</title>
    <script>
        (function() {
            try {
                document.addEventListener('DOMContentLoaded', function() {
                    var metas = document.querySelectorAll('meta[name="viewport"]');
                    metas.forEach(function(m) {
                        if (/target-densitydpi/i.test(m.content || '')) {
                            m.parentNode.removeChild(m);
                            console && console.log && console.log('Removed obsolete viewport meta with target-densitydpi');
                        }
                    });
                });
            } catch (e) {}
        })();
    </script>
    <style>
        body {
            margin: 0;
            height: 100vh;
            overflow: hidden;
            background: #f7f7f7;
        }

        iframe {
            width: 100%;
            height: 100%;
            border: none;
            position: absolute;
            top: 0;
            left: 0;
        }

        .blocker {
            position: fixed;
            inset: 0;
            z-index: 10;
            background: transparent;
            touch-action: none;
        }

        #status {
            position: fixed;
            bottom: 10px;
            left: 10px;
            font-family: Arial, sans-serif;
            background: rgba(255, 255, 255, 0.8);
            padding: 5px 10px;
            border-radius: 6px;
            font-size: 0.8rem;
            color: #333;
            z-index: 20;
        }
    </style>
</head>

<body>

    <!-- Embedded Slides -->
    <iframe
        id="slides"
        src="https://docs.google.com/presentation/d/1PgT7KC48KqXkt-r-3OPLfK6I6jV3JqpDUeZV8RTWkuw/embed?rm=minimal#slide=id.p1"
        allowfullscreen>
    </iframe>

    <!-- Transparent blocker so viewers can’t click the slides -->
    <div class="blocker"></div>

    <!-- Viewer message overlay -->
    <div id="viewerMessage" style="position:fixed; top:12px; right:12px; background:rgba(0,0,0,0.6); color:#fff; padding:8px 12px; border-radius:6px; z-index:30; display:none;"></div>

    <!-- Status text -->
    <div id="status">Waiting for host...</div>

    <script>
        // Reference to the slide iframe
        const slidesFrame = document.getElementById("slides");
        const statusText = document.getElementById("status");

        // Connect to Server-Sent Events stream
        const evtSource = new EventSource("slide_stream.php");
        let sseErrors = 0;
        let pollInterval = null;
        const startPolling = () => {
            if (pollInterval) return;
            console && console.log && console.log('SSE failed — starting polling fallback');
            statusText.textContent = 'Connection degraded — using polling';
            pollInterval = setInterval(() => {
                fetch('current_slide.json').then(r => r.json()).then(data => {
                    applyUpdate(data);
                }).catch(() => {});
            }, 1000);
        };

        const stopPolling = () => {
            if (!pollInterval) return;
            clearInterval(pollInterval);
            pollInterval = null;
        };

        // Shared update application used by SSE and polling
        const applyUpdate = (data) => {
            try {
                if (!data) return;
                if (data.slide) {
                    const base = 'https://docs.google.com/presentation/d/1PgT7KC48KqXkt-r-3OPLfK6I6jV3JqpDUeZV8RTWkuw/embed?rm=minimal';
                    const newSrc = `${base}&ts=${Date.now()}#slide=${data.slide}`;
                    if (slidesFrame.src !== newSrc) {
                        // force reload reliably: blank then set new src with cache-bust
                        try {
                            slidesFrame.src = 'about:blank';
                        } catch (e) {}
                        setTimeout(() => {
                            slidesFrame.src = newSrc;
                        }, 60);
                        statusText.textContent = "Now showing: " + data.slide;
                    }
                }
                if (data.message !== undefined) {
                    const vm = document.getElementById('viewerMessage');
                    vm.textContent = data.message;
                    vm.style.display = data.message ? 'block' : 'none';
                }
            } catch (e) {
                console.error(e);
            }
        };

        // On load, fetch current slide so we start synced immediately
        fetch('current_slide.json').then(r => r.json()).then(data => {
            if (data && data.slide) {
                const newSrc = `https://docs.google.com/presentation/d/1PgT7KC48KqXkt-r-3OPLfK6I6jV3JqpDUeZV8RTWkuw/embed?rm=minimal#slide=${data.slide}`;
                if (slidesFrame.src !== newSrc) {
                    slidesFrame.src = newSrc;
                    statusText.textContent = "Now showing: " + data.slide;
                }
                if (data.message) {
                    const vm = document.getElementById('viewerMessage');
                    vm.textContent = data.message;
                    vm.style.display = data.message ? 'block' : 'none';
                }
            }
        }).catch(() => {});

        evtSource.onmessage = function(e) {
            try {
                const data = JSON.parse(e.data);
                applyUpdate(data);
            } catch (err) {
                console.error("Bad SSE data", err);
                statusText.textContent = "Error reading update...";
            }
        };

        evtSource.onopen = function() {
            sseErrors = 0;
            stopPolling();
            statusText.textContent = 'Connected to host';
        };

        evtSource.onerror = function() {
            sseErrors += 1;
            statusText.textContent = 'Connection lost... retrying.';
            // after a few errors, fall back to polling because some extensions/blockers prevent SSE
            if (sseErrors >= 3) startPolling();
        };

        // (older code kept for reference) the above onerror handler now includes fallback logic

        // Prevent viewers from interacting
        window.addEventListener('keydown', e => e.preventDefault());
        window.addEventListener('touchstart', e => e.preventDefault(), {
            passive: false
        });
        window.addEventListener('touchmove', e => e.preventDefault(), {
            passive: false
        });
    </script>

</body>

</html>