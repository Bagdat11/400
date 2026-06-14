# templates.py

HTML_CONTROLLER = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Taldyk Summer - Ән Жазу</title>
    <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
</head>
<body class="h-screen bg-slate-950 text-white flex flex-col justify-between p-6 text-center select-none overflow-hidden">
    
    <div>
        <span class="text-xs font-bold text-fuchsia-500 uppercase tracking-widest">Taldyk Summer • Live AI DJ</span>
        <h1 class="text-xl font-black mt-1 text-cyan-400">ЖАНДЫ ПЛЕЙЛИСТ 🎵</h1>
        <p class="text-xs text-gray-400 mt-2">Кез келген ән атын (қазақша, орысша, шетелдік) жазыңыз. Жүйе оны интернеттен тауып, DJ Бит қосып ойнатады!</p>
    </div>

    <div class="bg-slate-900/80 border border-slate-800 p-6 rounded-2xl space-y-4 my-auto shadow-xl shadow-fuchsia-500/5">
        <h3 class="text-xs font-bold text-fuchsia-400 uppercase text-left">🎼 Ән немесе Орындаушы:</h3>
        <div class="flex flex-col gap-3">
            <input type="text" id="songInput" placeholder="Мысалы: Ауырмайды журек, 50k, Президент" 
                   class="w-full bg-slate-950 border border-slate-700 rounded-xl px-4 py-3 text-sm text-white focus:outline-none focus:border-cyan-400 placeholder:text-gray-600">
            <button onclick="sendSong()" class="w-full bg-gradient-to-r from-fuchsia-500 to-cyan-500 text-black font-black py-3 rounded-xl active:scale-95 transition text-sm tracking-wide">
                🚀 ӘНДІ ИНТЕРНЕТТЕН ТАБУ
            </button>
        </div>
    </div>

    <div class="bg-black/30 p-2 rounded-xl border border-white/5">
        <div id="status" class="text-emerald-400 text-[10px] font-bold">Байланыс орнатылуда...</div>
    </div>

    <script>
        const protocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:';
        const ws = new WebSocket(`${protocol}//${window.location.host}/ws`);
        
        ws.onopen = () => { document.getElementById('status').innerText = "БАЙЛАНЫС: БЕЛСЕНДІ 🌐"; };
        ws.onclose = () => { document.getElementById('status').innerText = "БАЙЛАНЫС ҮЗІЛДІ ❌"; };

        function sendSong() {
            const input = document.getElementById('songInput');
            const songName = input.value.trim();
            if (songName && ws.readyState === WebSocket.OPEN) {
                ws.send(JSON.stringify({ "type": "enqueue_song", "title": songName }));
                input.value = '';
                alert(`"${songName}" іздеуге жіберілді және кезекке қосылды! 🔎`);
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
        .neon-shadow { box-shadow: 0 0 50px #ef4444; }
    </style>
</head>
<body class="h-screen flex flex-col justify-between p-6 text-white overflow-hidden">
    
    <header class="w-full flex justify-between items-center border-b border-slate-800 pb-4">
        <div>
            <span class="text-xs font-bold text-fuchsia-500 tracking-widest uppercase">AI-DJ Cloud Remixer v5</span>
            <h1 class="text-2xl font-black tracking-wider text-white">TALDYK SUMMER <span class="text-cyan-400">LIVE SCREEN</span></h1>
        </div>
        <div class="bg-slate-900 border border-cyan-500/30 px-4 py-2 rounded-xl text-center">
            <span class="text-[10px] text-gray-400 block uppercase">ҚАЗІР НАҚТЫ ОЙНАП ТҰР:</span>
            <span id="currentPlaying" class="text-sm font-black text-green-400">ӘН КҮТУДЕ... 🎵</span>
        </div>
    </header>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-6 my-auto items-center">
        <div class="bg-slate-900/60 border border-slate-800 p-6 rounded-3xl space-y-4">
            <h2 class="text-sm font-black text-fuchsia-400 tracking-wider uppercase border-b border-slate-800 pb-2">📋 АЛДАҒЫ ӘНДЕР КЕЗЕГІ:</h2>
            <div id="queueList" class="space-y-2 text-xs">
                <p class="text-gray-500 text-center py-4">Кезек бос. Ән жазыңыз... 🎼</p>
            </div>
        </div>

        <div class="flex flex-col items-center justify-center relative h-64">
            <div id="ticker" class="absolute top-0 w-full text-center text-xs font-bold text-yellow-300 tracking-wide">
                Интернеттен тірі әндерді іздеу жүйесі қосылды! ✨
            </div>
            <div id="djBall" class="w-36 h-36 rounded-full bg-slate-900 border-4 border-slate-700 flex flex-col items-center justify-center transition-all duration-100 text-center p-2">
                <span id="ballStatus" class="text-[10px] font-black text-gray-500 uppercase">КҮТУДЕ</span>
                <span id="bpmText" class="text-[9px] text-cyan-400 font-mono mt-1"></span>
            </div>
            <div id="timerText" class="text-xs text-fuchsia-400 mt-4 font-mono h-4 font-bold"></div>
        </div>

        <div class="bg-slate-900/60 border border-slate-800 p-6 rounded-3xl text-xs space-y-2 text-gray-300">
            <p class="text-cyan-400 font-bold text-sm">🔥 РОБОТ-DJ ИННОВАЦИЯСЫ:</p>
            <p>• **Тірі іздеу:** Жүйе ашық музыкалық API-ден нағыз әннің аудиосын (mp3) лезде суырып алады.</p>
            <p>• **AI Бит Сплиттер:** Ән ойнап жатқанда, Web Audio API оның үстіне **128 BPM клубтық басс битін** қолдан жасап қосады.</p>
            <p class="text-fuchsia-400 font-medium mt-2">Нәтиже: Кез келген лирикалық ән бір секундта би алаңына арналған заманауи клубтық РЕМИКС-ке айналады!</p>
        </div>
    </div>

    <audio id="bgAudio" crossorigin="anonymous" style="display:none;"></audio>

    <footer class="w-full border-t border-slate-800 pt-4 flex justify-between items-center bg-slate-950 p-4 rounded-2xl">
        <div class="text-[10px] text-gray-500">TALDYK SUMMER REAL MUSIC DJ ENGINE v5</div>
        <div class="bg-white p-1 rounded-xl flex items-center gap-2">
            <img id="qrImg" src="" alt="QR" class="w-14 h-14">
            <div class="text-black text-left pr-2">
                <h4 class="text-[10px] font-black uppercase">Нағыз ән қос</h4>
                <p class="text-[8px] text-gray-500 mt-0.5">Сканерле де, атын жаз!</p>
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
        const queueList = document.getElementById('queueList');
        const timerText = document.getElementById('timerText');
        const ballStatus = document.getElementById('ballStatus');
        const bpmText = document.getElementById('bpmText');
        const bgAudio = document.getElementById('bgAudio');

        let songQueue = [];
        let isPlaying = false;
        let audioCtx = null;
        let beatInterval = null;

        function renderQueue() {
            if (songQueue.length === 0) {
                queueList.innerHTML = `<p class="text-gray-500 text-center py-4">Кезек бос. Ән жазыңыз... 🎼</p>`;
                return;
            }
            queueList.innerHTML = "";
            songQueue.forEach((song, index) => {
                queueList.innerHTML += `
                    <div class="flex justify-between items-center bg-slate-950 p-3 rounded-xl border border-slate-800">
                        <span class="font-bold text-white">${index + 1}. 🎵 ${song}</span>
                        <span class="text-[9px] text-fuchsia-400 uppercase font-mono tracking-wider">Күтуде</span>
                    </div>
                `;
            });
        }

        // КЕРЕМЕТ ИДЕЯ: ИНТЕРНЕТТЕН (DEEZER АРҚЫЛЫ) НАҒЫЗ MP3 ТАБУ ФУНКЦИЯСЫ
        async doFetchAndPlay() {
            if (songQueue.length === 0) {
                isPlaying = false;
                currentPlaying.innerText = "ӘН КҮТУДЕ... 🎵";
                ballStatus.innerText = "КҮТУДЕ";
                bpmText.innerText = "";
                djBall.style.backgroundColor = '#0f172a';
                djBall.style.boxShadow = 'none';
                timerText.innerText = "";
                if (beatInterval) clearInterval(beatInterval);
                return;
            }

            isPlaying = true;
            let querySong = songQueue.shift();
            renderQueue();

            ticker.innerText = `🔎 Интернеттен ізделуде: "${querySong}"...`;
            currentPlaying.innerText = `ТАБЫЛУДА: ${querySong}...`;

            try {
                // Deezer-дің ашық API-іне сұраныс жіберіп, әнді іздейміз
                let response = await fetch(`https://api.allorigins.win/get?url=${encodeURIComponent('https://api.deezer.com/search?q=' + querySong)}`);
                let resData = await response.json();
                let searchResult = JSON.parse(resData.contents);

                if (searchResult.data && searchResult.data.length > 0) {
                    let track = searchResult.data[0]; // Ең бірінші шыққан ресми тректі аламыз
                    let mpUrl = track.preview; // Оның 30 секундтық тірі mp3 сілтемесі
                    let realTitle = track.title + " - " + track.artist.name;

                    currentPlaying.innerText = realTitle.toUpperCase();
                    ballStatus.innerText = "LIVE REMIX";
                    bpmText.innerText = "🔥 +128 BPM BASS";
                    djBall.style.backgroundColor = '#ef4444'; // Қызыл түс (Жанды дискотека)
                    djBall.style.boxShadow = '0 0 50px #ef4444';

                    // Аудионы ойнату
                    bgAudio.src = mpUrl;
                    bgAudio.play();

                    // Тірілей электронды гүн-гүн бит (Бассты) қосу циклі
                    if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
                    if (beatInterval) clearInterval(beatInterval);

                    // Клубтық 128 BPM ырғақ (әр 450 миллисекунд сайын ауыр басс соғады)
                    beatInterval = setInterval(() => {
                        const osc = audioCtx.createOscillator();
                        const gain = audioCtx.createGain();
                        osc.connect(gain);
                        gain.connect(audioCtx.destination);
                        
                        osc.type = 'sine';
                        osc.frequency.setValueAtTime(65, audioCtx.currentTime); // Өте төмен, ауыр фестивальдік БАСС (ГҮН)
                        gain.gain.setValueAtTime(1.2, audioCtx.currentTime);
                        gain.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.2);
                        
                        osc.start();
                        osc.stop(audioCtx.currentTime + 0.2);

                        // Шарды нағыз битпен секірту
                        djBall.style.transform = 'scale(1.18)';
                        setTimeout(() => djBall.style.transform = 'scale(1)', 80);
                    }, 450);

                    // Ән аяқталғанда немесе 25 секундтан кейін келесі әнді автоматты қосу
                    let timeLeft = 25;
                    timerText.innerText = `⏳ Ремикс уақыты: ${timeLeft} сек`;
                    
                    let countdown = setInterval(() => {
                        timeLeft--;
                        if (timeLeft > 0 && isPlaying) {
                            timerText.innerText = `⏳ Ремикс уақыты: ${timeLeft} сек`;
                        } else {
                            clearInterval(countdown);
                        }
                    }, 1000);

                    setTimeout(() => {
                        bgAudio.pause();
                        if (beatInterval) clearInterval(beatInterval);
                        doFetchAndPlay(); // Келесі әнді қосу
                    }, 25000);

                } else {
                    ticker.innerText = `❌ "${querySong}" интернеттен табылмады, келесіге көшеміз.`;
                    setTimeout(() => { doFetchAndPlay(); }, 2000);
                }
            } catch (err) {
                ticker.innerText = "⚠️ Желілік қате, келесі тректі іске қосамыз...";
                setTimeout(() => { doFetchAndPlay(); }, 2000);
            }
        }

        ws.onmessage = (event) => {
            const data = JSON.parse(event.data);
            if (data.type === "enqueue_song") {
                ticker.innerText = `⚡ КЕЗЕККЕ ЖАҢА ӘН ТҮСТІ: "${data.title}"`;
                songQueue.push(data.title);
                renderQueue();

                if (!isPlaying) {
                    doFetchAndPlay();
                }
            }
        };
    </script>
</body>
</html>
"""
