# templates.py

HTML_CONTROLLER = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Taldyk Summer Controller</title>
    <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
</head>
<body class="h-screen bg-slate-950 text-white flex flex-col justify-between p-6 text-center select-none overflow-hidden">
    
    <div>
        <span class="text-xs font-bold text-fuchsia-500 uppercase tracking-widest">Taldyk Summer • Live DJ</span>
        <h1 class="text-xl font-black mt-1 text-cyan-400">AI REMOTE INTERACTIVE</h1>
    </div>

    <div class="flex flex-col items-center justify-center my-4">
        <div id="pad" class="w-48 h-48 rounded-full border-4 border-dashed border-fuchsia-500 flex items-center justify-center animate-pulse shadow-xl shadow-fuchsia-500/10">
            <div class="text-xs font-bold text-fuchsia-400">ТЕЛЕФОНДЫ СІЛКІҢІЗ<br>БИТ ШЫҒАРУ СИГНАЛЫ 🎵</div>
        </div>
    </div>

    <div class="bg-slate-900/80 border border-slate-800 p-4 rounded-2xl space-y-3">
        <h3 class="text-xs font-bold text-gray-400 uppercase text-left">📺 Экранға хабарлама жіберу:</h3>
        <div class="flex gap-2">
            <input type="text" id="msgInput" placeholder="Сәлем, Талдықорған! немесе Insta" class="w-full bg-slate-950 border border-slate-700 rounded-xl px-3 py-2 text-sm text-white focus:outline-none focus:border-cyan-400">
            <button onclick="sendMessage()" class="bg-cyan-500 text-black font-bold text-xs px-4 rounded-xl active:scale-95 transition">Жіберу</button>
        </div>
    </div>

    <div class="bg-black/30 p-3 rounded-xl border border-white/5">
        <div id="status" class="text-emerald-400 text-xs font-bold">Байланыс орнатылуда...</div>
    </div>

    <script>
        // Протоколды (ws немесе wss) сервердің түріне қарай автоматты таңдау
        const protocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:';
        const ws = new WebSocket(`${protocol}//${window.location.host}/ws`);
        
        ws.onopen = () => {
            document.getElementById('status').innerText = "БАЙЛАНЫС: БЕЛСЕНДІ 🌐";
        };

        ws.onclose = () => {
            document.getElementById('status').innerText = "БАЙЛАНЫС ҮЗІЛДІ ❌";
        };

        if (window.DeviceMotionEvent) {
            window.addEventListener('devicemotion', (event) => {
                let x = event.accelerationIncludingGravity.x || 0;
                let y = event.accelerationIncludingGravity.y || 0;
                let z = event.accelerationIncludingGravity.z || 0;

                if (ws.readyState === WebSocket.OPEN) {
                    ws.send(JSON.stringify({ "type": "motion", "x": x, "y": y, "z": z }));
                }
            });
        }

        function sendMessage() {
            const input = document.getElementById('msgInput');
            const text = input.value.trim();
            if (text && ws.readyState === WebSocket.OPEN) {
                ws.send(JSON.stringify({ "type": "message", "text": text }));
                input.value = '';
                alert("Хабарлама үлкен экранға жіберілді! 🚀");
            }
        }
    </script>
</body>
</html>
"""

HTML_DASHBOARD = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Taldyk Summer Screen Hub</title>
    <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght=700;900&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Orbitron', sans-serif; background: radial-gradient(circle, #020617 0%, #000000 100%); }
        .neon-shadow { box-shadow: 0 0 50px #00f0ff; }
    </style>
</head>
<body class="h-screen flex flex-col justify-between p-6 md:p-10 text-white overflow-hidden">
    
    <header class="w-full flex justify-between items-center border-b border-slate-800 pb-4">
        <div>
            <span class="text-xs font-bold text-cyan-400 uppercase tracking-widest">Interactive Tech Zone</span>
            <h1 class="text-3xl font-black tracking-wider text-white">TALDYK SUMMER <span class="text-fuchsia-500">LIVE ENGINE</span></h1>
        </div>
        <div class="bg-slate-900 border border-cyan-500/30 px-4 py-2 rounded-xl text-center">
            <span class="text-[10px] text-gray-400 block uppercase">Жанды сигналдар</span>
            <span id="signalCount" class="text-sm font-bold text-cyan-400">0 Hz</span>
        </div>
    </header>

    <div class="relative w-full h-96 flex flex-col items-center justify-center">
        <div id="ticker" class="absolute top-4 w-full text-center text-xl font-bold text-yellow-300 tracking-wide animate-pulse">
            Сәлемдеме күтуде... ✨
        </div>

        <div id="djBall" class="w-32 h-32 rounded-full bg-cyan-500 border-4 border-white neon-shadow flex items-center justify-center transition-all duration-75">
            <span class="text-xs font-black text-black">AI AUDIO</span>
        </div>
        
        <div id="boomEffect" class="hidden text-6xl font-black text-transparent bg-clip-text bg-gradient-to-r from-fuchsia-500 to-cyan-400 mt-6 animate-ping">
            💥 DJ BEAT DROP! 💥
        </div>
    </div>

    <footer class="w-full border-t border-slate-800 pt-4 flex flex-col md:flex-row justify-between items-center bg-slate-950 p-6 rounded-3xl gap-4">
        <div class="text-xs text-gray-400 space-y-1">
            <p>🚀 <strong class="text-white">ИНВЕСТОРЛАР МЕН ЖЮРИГЕ АРНАЛҒАН БИЗНЕС-МОДЕЛЬ:</strong></p>
            <p>Қонақтар өз телефондарын джойстик қылып, демеушілердің интерактивті логотиптерін ашады.</p>
        </div>
        <div class="bg-white p-2 rounded-2xl flex items-center gap-3">
            <img id="qrImg" src="" alt="QR" class="w-20 h-20">
            <div class="text-black text-left pr-2">
                <h4 class="text-xs font-black uppercase">Пультке қосылу</h4>
                <p class="text-[9px] text-gray-500 leading-tight mt-0.5">Камерамен сканерлеп,<br>экранды басқарыңыз!</p>
            </div>
        </div>
    </footer>

    <script>
        // Сүйемелдеуші динамикалық QR код сілтемесі
        const currentUrl = window.location.protocol + '//' + window.location.host + '/phone';
        document.getElementById('qrImg').src = `https://api.qrserver.com/v1/create-qr-code/?size=120x120&data=${encodeURIComponent(currentUrl)}`;

        // Протоколды (ws немесе wss) автоматты түрде анықтау
        const protocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:';
        const ws = new WebSocket(`${protocol}//${window.location.host}/ws`);
        
        const djBall = document.getElementById('djBall');
        const boomEffect = document.getElementById('boomEffect');
        const ticker = document.getElementById('ticker');
        const signalCount = document.getElementById('signalCount');
        
        let signalHz = 0;
        let audioCtx = null;
        
        function playBeat() {
            if (!audioCtx) {
                audioCtx = new (window.AudioContext || window.webkitAudioContext)();
            }
            const osc = audioCtx.createOscillator();
            const gain = audioCtx.createGain();
            osc.connect(gain);
            gain.connect(audioCtx.destination);
            
            osc.type = 'sine';
            osc.frequency.setValueAtTime(130, audioCtx.currentTime);
            gain.gain.setValueAtTime(1, audioCtx.currentTime);
            
            gain.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.3);
            osc.start();
            osc.stop(audioCtx.currentTime + 0.3);
        }

        ws.onmessage = (event) => {
            const data = JSON.parse(event.data);
            signalHz++;
            signalCount.innerText = `${signalHz} Hz`;

            if (data.type === "motion") {
                let moveX = data.x * 35;
                let moveY = data.y * -35;
                let totalForce = Math.abs(data.x) + Math.abs(data.y);

                djBall.style.transform = `translate(${moveX}px, ${moveY}px) rotate(${data.z * 10}deg)`;

                if (totalForce > 24) {
                    playBeat();
                    djBall.style.backgroundColor = '#f43f5e';
                    djBall.style.boxShadow = '0 0 70px #f43f5e';
                    boomEffect.classList.remove('hidden');
                    
                    setTimeout(() => {
                        djBall.style.backgroundColor = '#06b6d4';
                        djBall.style.boxShadow = '0 0 50px #00f0ff';
                        boomEffect.classList.add('hidden');
                    }, 400);
                }
            }

            if (data.type === "message") {
                ticker.innerText = `💬 ҚОНАҚ: "${data.text}"`;
                ticker.classList.add('text-green-400', 'text-2xl');
                setTimeout(() => {
                    ticker.classList.remove('text-green-400', 'text-2xl');
                }, 3000);
            }
        };
    </script>
</body>
</html>
"""
