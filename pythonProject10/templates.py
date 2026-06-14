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
        <h1 class="text-xl font-black mt-1 text-cyan-400">DJ MUSIC VOTE 🎵</h1>
    </div>

    <div class="bg-slate-900/60 border border-slate-800 p-4 rounded-2xl space-y-3 my-2">
        <h3 class="text-xs font-bold text-fuchsia-400 uppercase text-left">🔥 Қазір қандай БИТ ойнасын?</h3>
        <div class="grid grid-cols-1 gap-2">
            <button onclick="voteMusic('🚨 TECHNO CLUB')" class="bg-gradient-to-r from-fuchsia-600 to-pink-600 text-white font-bold py-3 rounded-xl active:scale-95 transition text-sm shadow-lg shadow-pink-500/20">
                🚨 TECHNO CLUB БИТ жіберу
            </button>
            <button onclick="voteMusic('🌴 SUMMER HOUSE')" class="bg-gradient-to-r from-cyan-600 to-blue-600 text-white font-bold py-3 rounded-xl active:scale-95 transition text-sm shadow-lg shadow-cyan-500/20">
                🌴 SUMMER HOUSE БИТ жіберу
            </button>
            <button onclick="voteMusic('🥁 HIP-HOP BEAT')" class="bg-gradient-to-r from-amber-500 to-orange-600 text-white font-bold py-3 rounded-xl active:scale-95 transition text-sm shadow-lg shadow-orange-500/20">
                🥁 HIP-HOP BEAT БИТ жіберу
            </button>
        </div>
    </div>

    <div class="bg-slate-900/80 border border-slate-800 p-4 rounded-2xl space-y-3">
        <h3 class="text-xs font-bold text-gray-400 uppercase text-left">📺 Экранға хабарлама жіберу:</h3>
        <div class="flex gap-2">
            <input type="text" id="msgInput" placeholder="Сәлем, Талдықорған!" class="w-full bg-slate-950 border border-slate-700 rounded-xl px-3 py-2 text-sm text-white focus:outline-none focus:border-cyan-400">
            <button onclick="sendMessage()" class="bg-cyan-500 text-black font-bold text-xs px-4 rounded-xl active:scale-95 transition">Жіберу</button>
        </div>
    </div>

    <div class="bg-black/30 p-2 rounded-xl border border-white/5">
        <div id="status" class="text-emerald-400 text-[10px] font-bold">Байланыс орнатылуда...</div>
    </div>

    <script>
        const protocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:';
        const ws = new WebSocket(`${protocol}//${window.location.host}/ws`);
        
        ws.onopen = () => {
            document.getElementById('status').innerText = "БАЙЛАНЫС: БЕЛСЕНДІ 🌐";
        };
        ws.onclose = () => {
            document.getElementById('status').innerText = "БАЙЛАНЫС ҮЗІЛДІ ❌";
        };

        // Музыкаға дауыс беру функциясы
        function voteMusic(trackName) {
            if (ws.readyState === WebSocket.OPEN) {
                ws.send(JSON.stringify({ "type": "vote", "track": trackName }));
                alert(`"${trackName}" әніне дауыс берілді! 🚀`);
            }
        }

        function sendMessage() {
            const input = document.getElementById('msgInput');
            const text = input.value.trim();
            if (text && ws.readyState === WebSocket.OPEN) {
                ws.send(JSON.stringify({ "type": "message", "text": text }));
                input.value = '';
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
<body class="h-screen flex flex-col justify-between p-6 text-white overflow-hidden">
    
    <header class="w-full flex justify-between items-center border-b border-slate-800 pb-4">
        <div>
            <span class="text-xs font-bold text-cyan-400 uppercase tracking-widest">Interactive Tech Zone</span>
            <h1 class="text-2xl font-black tracking-wider text-white">TALDYK SUMMER <span class="text-fuchsia-500">LIVE ENGINE</span></h1>
        </div>
        <div class="bg-slate-900 border border-cyan-500/30 px-4 py-2 rounded-xl text-center">
            <span class="text-[10px] text-gray-400 block uppercase">Қазір ойнап тұр:</span>
            <span id="currentPlaying" class="text-xs font-bold text-green-400">КҮТУДЕ... 🎵</span>
        </div>
    </header>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-6 my-auto items-center">
        <div class="bg-slate-900/60 border border-slate-800 p-6 rounded-3xl space-y-4">
            <h2 class="text-sm font-black text-fuchsia-400 tracking-wider uppercase border-b border-slate-800 pb-2">📊 ӘНДЕР РЕЙТИНГІ:</h2>
            <div class="space-y-3">
                <div>
                    <div class="flex justify-between text-xs mb-1"><span>🚨 Techno Club</span><span id="v-techno" class="font-bold text-pink-500">0 дауыс</span></div>
                    <div class="w-full bg-slate-950 h-2 rounded-full"><div id="p-techno" class="bg-pink-500 h-2 rounded-full transition-all" style="width: 0%"></div></div>
                </div>
                <div>
                    <div class="flex justify-between text-xs mb-1"><span>🌴 Summer House</span><span id="v-house" class="font-bold text-cyan-400">0 дауыс</span></div>
                    <div class="w-full bg-slate-950 h-2 rounded-full"><div id="p-house" class="bg-cyan-400 h-2 rounded-full transition-all" style="width: 0%"></div></div>
                </div>
                <div>
                    <div class="flex justify-between text-xs mb-1"><span>🥁 Hip-Hop Beat</span><span id="v-hiphop" class="font-bold text-amber-400">0 дауыс</span></div>
                    <div class="w-full bg-slate-950 h-2 rounded-full"><div id="p-hiphop" class="bg-amber-400 h-2 rounded-full transition-all" style="width: 0%"></div></div>
                </div>
            </div>
        </div>

        <div class="flex flex-col items-center justify-center relative h-64">
            <div id="ticker" class="absolute top-0 w-full text-center text-lg font-bold text-yellow-300 tracking-wide">
                Сәлемдеме күтуде... ✨
            </div>
            <div id="djBall" class="w-32 h-32 rounded-full bg-cyan-500 border-4 border-white neon-shadow flex items-center justify-center transition-all duration-300">
                <span class="text-xs font-black text-black text-center">LIVE<br>BEAT</span>
            </div>
        </div>

        <div class="bg-slate-900/60 border border-slate-800 p-6 rounded-3xl text-xs space-y-2 text-gray-300">
            <p class="text-fuchsia-400 font-bold text-sm">💡 СТАРТАП МОНЕТИЗАЦИЯСЫ:</p>
            <p>• 1 дауыс беру = Тегін (немесе демеуші жарнамасы)</p>
            <p>• Өз әніңді кезексіз бірінші ойнату = 500 ₸ (Донат жүйесі)</p>
            <p class="text-cyan-400 font-medium mt-2">Қонақтар DJ пультін өздері басқарып, кештің интерактивтілігін 400%-ға арттырады.</p>
        </div>
    </div>

    <footer class="w-full border-t border-slate-800 pt-4 flex justify-between items-center bg-slate-950 p-4 rounded-2xl">
        <div class="text-[10px] text-gray-500">TALDYK SUMMER LIVE AUDIO SYSTEM V2</div>
        <div class="bg-white p-1 rounded-xl flex items-center gap-2">
            <img id="qrImg" src="" alt="QR" class="w-14 h-14">
            <div class="text-black text-left pr-2">
                <h4 class="text-[10px] font-black uppercase">Ән таңдау</h4>
                <p class="text-[8px] text-gray-500 mt-0.5">Сканерлеп дауыс бер!</p>
            </div>
        </div>
    </footer>

    <script>
        const currentUrl = window.location.protocol + '//' + window.location.host + '/phone';
        document.getElementById('qrImg').src = `https://api.qrserver.com/v1/create-qr-code/?size=100x100&data=${encodeURIComponent(currentUrl)}`;

        const protocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:';
        const ws = new WebSocket(`${protocol}//${window.location.host}/ws`);
        
        const djBall = document.getElementById('djBall');
        const ticker = document.getElementById('ticker');
        const currentPlaying = document.getElementById('currentPlaying');

        // Дауыс санағыш айнымалылар
        let votes = { "🚨 TECHNO CLUB": 0, "🌴 SUMMER HOUSE": 0, "🥁 HIP-HOP BEAT": 0 };
        let audioCtx = null;
        let currentInterval = null;

        // Жоба ішінде дыбыс генераторы (Web Audio API) - СЕРВЕРСІЗ-АҚ СИНТЕЗДЕУ
        function startMusicSynth(type) {
            if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
            if (currentInterval) clearInterval(currentInterval);

            let freq = 100; // Әдепкі басс жиілігі
            let speed = 500; // Бит жылдамдығы (микросекунд)

            if (type === "🚨 TECHNO CLUB") { freq = 140; speed = 300; djBall.style.backgroundColor = '#ec4899'; }
            if (type === "🌴 SUMMER HOUSE") { freq = 110; speed = 400; djBall.style.backgroundColor = '#06b6d4'; }
            if (type === "🥁 HIP-HOP BEAT") { freq = 80; speed = 600; djBall.style.backgroundColor = '#f59e0b'; }

            currentPlaying.innerText = type;

            // Битті үздіксіз автоматты ойнату циклі
            currentInterval = setInterval(() => {
                const osc = audioCtx.createOscillator();
                const gain = audioCtx.createGain();
                osc.connect(gain);
                gain.connect(audioCtx.destination);
                
                osc.type = 'triangle';
                osc.frequency.setValueAtTime(freq, audioCtx.currentTime);
                gain.gain.setValueAtTime(0.8, audioCtx.currentTime);
                gain.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.2);
                
                osc.start();
                osc.stop(audioCtx.currentTime + 0.2);

                // Шарды бит ырғағымен секірту
                djBall.style.transform = 'scale(1.2)';
                setTimeout(() => djBall.style.transform = 'scale(1)', 100);
            }, speed);
        }

        // Дауыс беруді есептеп, экранды тірілей жаңарту логикасы
        function updateRating() {
            let total = votes["🚨 TECHNO CLUB"] + votes["🌴 SUMMER HOUSE"] + votes["🥁 HIP-HOP BEAT"] || 1;
            
            document.getElementById('v-techno').innerText = `${votes["🚨 TECHNO CLUB"]} дауыс`;
            document.getElementById('p-techno').style.width = `${(votes["🚨 TECHNO CLUB"] / total) * 100}%`;

            document.getElementById('v-house').innerText = `${votes["🌴 SUMMER HOUSE"]} дауыс`;
            document.getElementById('p-house').style.width = `${(votes["🌴 SUMMER HOUSE"] / total) * 100}%`;

            document.getElementById('v-hiphop').innerText = `${votes["🥁 HIP-HOP BEAT"]} дауыс`;
            document.getElementById('p-hiphop').style.width = `${(votes["🥁 HIP-HOP BEAT"] / total) * 100}%`;

            // Ең көп дауыс жинаған әнді анықтау
            let winner = Object.keys(votes).reduce((a, b) => votes[a] >= votes[b] ? a : b);
            if (votes[winner] > 0) {
                startMusicSynth(winner);
            }
        }

        ws.onmessage = (event) => {
            const data = JSON.parse(event.data);

            if (data.type === "vote") {
                votes[data.track]++;
                ticker.innerText = `⚡ ЖАҢА ДАУЫС: ${data.track}!`;
                updateRating();
            }

            if (data.type === "message") {
                ticker.innerText = `💬 ҚОНАҚ: "${data.text}"`;
            }
        };
    </script>
</body>
</html>
"""
