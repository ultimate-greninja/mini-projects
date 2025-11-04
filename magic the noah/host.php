<?php
session_start();
if (empty($_SESSION['is_host'])) {
    header('Location: index.php');
    exit;
}

// The Google Slides embed link
$slidesUrl = "https://docs.google.com/presentation/d/1PgT7KC48KqXkt-r-3OPLfK6I6jV3JqpDUeZV8RTWkuw/embed?start=false&loop=false&rm=minimal";
?>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width,initial-scale=1.0">
    <title>Host — Magic the Noah</title>
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
            font-family: Arial, sans-serif;
            margin: 0;
            background: #f0f2f5;
            display: flex;
            flex-direction: column;
            height: 100vh;
        }

        header {
            background: #007bff;
            color: #fff;
            padding: 1rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .controls {
            display: flex;
            justify-content: center;
            gap: 1rem;
            background: #fff;
            padding: 1rem;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }

        button {
            padding: 0.8rem 1.6rem;
            font-size: 1rem;
            border: none;
            border-radius: 6px;
            background: #007bff;
            color: #fff;
            cursor: pointer;
            transition: background 0.2s;
        }

        button:hover {
            background: #0056b3;
        }

        iframe {
            flex: 1;
            width: 100%;
            border: none;
        }

        .logout {
            background: #dc3545;
        }

        #status {
            text-align: center;
            font-size: 0.9rem;
            color: #333;
            padding: 0.5rem 0;
        }
    </style>
</head>

<body>

    <header>
        <h2>Magic the Noah — Host</h2>
        <form action="logout.php" method="post">
            <button class="logout">Logout</button>
        </form>
    </header>

    <div class="controls">
        <button onclick="prevSlide()">⬅ Previous</button>
        <button onclick="nextSlide()">Next ➡</button>
        <div style="display:flex; align-items:center; gap:8px; margin-left:16px;">
            <input id="jumpInput" type="number" min="1" placeholder="#" style="width:70px; padding:6px; border-radius:4px; border:1px solid #ccc;" />
            <button onclick="jumpTo()">Jump</button>
        </div>
    </div>

    <iframe
        id="slideFrame"
        src="<?php echo $slidesUrl; ?>"
        allowfullscreen>
    </iframe>

    <p id="status">Ready to control slides.</p>

    <div style="padding:12px; background:#fff; box-shadow:0 1px 3px rgba(0,0,0,0.08);">
        <label style="font-size:0.9rem; margin-right:8px">Viewer message:</label>
        <input id="viewerMsg" type="text" placeholder="Message for viewers" style="width:60%; padding:6px; border-radius:4px; border:1px solid #ccc;" />
        <button onclick="sendMessage()">Send</button>
    </div>

    <script>
        const frame = document.getElementById('slideFrame');
        const statusText = document.getElementById('status');

        // Track slide index locally and tell viewers which fragment to open.
        // We can't reliably drive the Google Slides iframe via postMessage (cross-origin),
        // so we update `current_slide.json` with a slide fragment like "id.p1".
        let slideIndex = 1; // start at first slide
        const slidePrefix = 'id.p';

        function updateSlideState(fragment) {
            fetch('update_slide.php', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    slide: fragment
                })
            }).catch(err => console.error(err));
        }

        function setIframeToCurrent() {
            const base = '<?php echo $slidesUrl; ?>';
            const newSrc = `${base}#slide=${slidePrefix}${slideIndex}&ts=${Date.now()}`;
            if (frame.src !== newSrc) {
                try {
                    frame.src = 'about:blank';
                } catch (e) {}
                setTimeout(() => {
                    frame.src = newSrc;
                }, 60);
            }
        }

        // On load, sync with current_slide.json so host and viewers start aligned
        fetch('current_slide.json').then(r => r.json()).then(data => {
            if (data && data.slide) {
                // data.slide expected like 'id.p3'
                const match = data.slide.match(/id\.p(\d+)/);
                if (match) {
                    slideIndex = parseInt(match[1], 10) || 1;
                }
                setIframeToCurrent();
                statusText.textContent = `Ready (showing slide ${slideIndex})`;
            }
        }).catch(() => {
            // ignore and use defaults
        });

        // Move to next slide
        function nextSlide() {
            slideIndex += 1;
            setIframeToCurrent();
            updateSlideState(slidePrefix + slideIndex);
            statusText.textContent = `Moved to slide ${slideIndex}`;
        }

        function jumpTo() {
            const n = parseInt(document.getElementById('jumpInput').value, 10);
            if (!isNaN(n) && n > 0) {
                slideIndex = n;
                setIframeToCurrent();
                updateSlideState(slidePrefix + slideIndex);
                statusText.textContent = `Jumped to ${slideIndex}`;
            }
        }

        function sendMessage() {
            const msg = document.getElementById('viewerMsg').value || '';
            fetch('update_slide.php', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    message: msg
                })
            }).then(() => {
                statusText.textContent = 'Message sent';
            }).catch(() => statusText.textContent = 'Message send failed');
        }

        // Move to previous slide
        function prevSlide() {
            if (slideIndex > 1) slideIndex -= 1;
            setIframeToCurrent();
            updateSlideState(slidePrefix + slideIndex);
            statusText.textContent = `Moved to slide ${slideIndex}`;
        }

        // Allow arrow keys too
        window.addEventListener('keydown', e => {
            if (e.key === 'ArrowRight') nextSlide();
            if (e.key === 'ArrowLeft') prevSlide();
        });
    </script>

</body>

</html>