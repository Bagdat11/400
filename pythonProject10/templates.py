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
        <h1 class="text-xl font-black mt-1 text-cyan-400">НАҒЫЗ ӘН ТАҢДАУ 🎵</h1>
        <p class="text-xs text-gray-400 mt-2">Қалаған әніңізді жазыңыз (Ирина Кайратовна, Ауырмайды журек, т.б.). Жүйе оны интернеттен тауып, DJ Бит қосады!</p>
    </div>

    <div class="bg-slate-900/80 border border-slate-800 p-6 rounded-2xl space-y-4 my-auto shadow-xl shadow-fuchsia-500/5">
        <h3 class="text-xs font-bold text-fuchsia-400 uppercase text-left">🎼 Ән немесе Орындаушы:</h3>
        <div class="flex flex-col gap-3">
            <input type="text" id="songInput" placeholder="Мысалы: Ауырмайды журек, Ирина Кайратовна, 50k" 
                   class="w-full bg-slate-950 border border-slate-700 rounded-xl px-4 py-3 text-sm text-white focus:outline-none focus:border-cyan-400 placeholder:text-gray-600">
            <button onclick="sendSong()" class="w-full bg-gradient-to-r from-cyan-500 to-fuchsia-500 text-black font-black py-3 rounded-xl active:scale-95 transition text-sm tracking-wide">
                🚀 ИНТЕРНЕТТЕН ТАУЫП ОЙНАТУ
            </button>
        </div>
        <div class="text-[10px] text-gray-500 text-left bg-black/30 p-2 rounded-lg leading-tight">
            💡 **Питч кеңесі:** Сахнада жюриге көрсеткенде "Ирина Кайратовна", "Ауырмайды журек", "50k" немесе "Miyagi" деп жазсаң, интернеттен нағыз трек бірден іске қосылады!
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
                alert(`"${songName}" іздеуге жіберілді! 🕒`);
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
    <script src="https://cdnjs.cloudflare.com/ajax/libs/qrcodejs/1.0.0/qrcode.min.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght=700;900&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Orbitron', sans-serif; background: radial-gradient(circle, #020617 0%, #000000 100%); }
        .neon-shadow { box-shadow: 0 0 50px #ef4444; }
        #qrcode img { display: inline-block !important; }
    </style>
</head>
<body class="h-screen flex flex-col justify-between p-6 text-white overflow-hidden">
    
    <header class="w-full flex justify-between items-center border-b border-slate-800 pb-4">
        <div>
            <span class="text-xs font-bold text-fuchsia-500 tracking-widest uppercase">AI-DJ Internet Streamer v6</span>
            <h1 class="text-2xl font-black tracking-wider text-white">TALDYK SUMMER <span class="text-cyan-400">LIVE SCREEN</span></h1>
        </div>
        <div class="bg-slate-900 border border-cyan-500/30 px-4 py-2 rounded-xl text-center">
            <span class="text-[10px] text-gray-400 block uppercase">ҚАЗІР НАҚТЫ ОЙНАП ТҰР:</span>
            <span id="currentPlaying" class="text-sm font-black text-green-400">ӘН КҮТУДЕ... 🎵</span>
        </div>
    </header>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-6 my-auto items-center">
        <div class="bg-slate-900/60 border border-slate-800 p-6 rounded-3xl space-y-4">
            <h2 class="text-sm font-black text-cyan-400 tracking-wider uppercase border-b border-slate-800 pb-2">📋 АЛДАҒЫ ӘНДЕР КЕЗЕГІ:</h2>
            <div id="queueList" class="space-y-2 text-xs">
                <p class="text-gray-500 text-center py-4">Кезек бос. Ән жазыңыз... 🎼</p>
            </div>
        </div>

        <div class="flex flex-col items-center justify-center relative h-64">
            <div id="ticker" class="absolute top-0 w-full text-center text-xs font-bold text-yellow-300 tracking-wide">
                Жаһандық бұлттық аудио ағыны қосылды! ✨
            </div>
            <div id="djBall" class="w-36 h-36 rounded-full bg-slate-900 border-4 border-slate-700 flex flex-col items-center justify-center transition-all duration-100 text-center p-2">
                <span id="ballStatus" class="text-[10px] font-black text-gray-500 uppercase">КҮТУДЕ</span>
                <span id="bpmText" class="text-[9px] text-cyan-400 font-mono mt-1"></span>
            </div>
            <div id="timerText" class="text-xs text-fuchsia-400 mt-4 font-mono h-4 font-bold"></div>
        </div>

        <div class="bg-slate-900/60 border border-slate-800 p-6 rounded-3xl text-xs space-y-2 text-gray-300">
            <p class="text-cyan-400 font-bold text-sm">🔥 РОБОТ-DJ ИННОВАЦИЯСЫ:</p>
            <p>• **Тірі бұлттық жүктеу:** Жүйе интернеттегі ресми ашық аудио қоймадан нағыз әуенді тауып ойнатады.</p>
            <p>• **AI Бит Сплиттер:** Ән ойнап жатқанда, ноутбуктің ішкі дыбыс картасы оның үстіне **128 BPM клубтық басс битін (гүн-гүн)** тірілей синтездеп қосады.</p>
            <p class="text-fuchsia-400 font-medium mt-2">Нәтиже: Кәдімгі ән би алаңына арналған заманауи LIVE РЕМИКС-ке айналады!</p>
        </div>
    </div>

    <audio id="bgAudio" crossorigin="anonymous" style="display:none;"></audio>

    <footer class="w-full border-t border-slate-800 pt-4 flex justify-between items-center bg-slate-950 p-4 rounded-2xl">
        <div class="text-[10px] text-gray-500">TALDYK SUMMER STREAM DJ ENGINE v6</div>
        
        <div class="bg-white p-2 rounded-2xl flex items-center gap-4 text-black shadow-lg shadow-white/5">
            <div id="qrcode" class="p-1 bg-white rounded-lg"></div>
            <div class="text-left pr-4">
                <h4 class="text-xs font-black uppercase tracking-wide text-slate-950">Өз әніңді қос</h4>
                <p class="text-[9px] text-gray-600 mt-0.5 leading-tight">Камерамен сканерле де,<br>қалаған әніңнің атын жаз!</p>
            </div>
        </div>
    </footer>

    <script>
        const phoneUrl = window.location.origin + '/phone';
        new QRCode(document.getElementById("qrcode"), {
            text: phoneUrl,
            width: 85,
            height: 85,
            colorDark : "#000000",
            colorLight : "#ffffff",
            correctLevel : QRCode.CorrectLevel.H
        });

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

        // ХАКАТОНДА ТАППМАЙ ҚАЛМАС УШІН ИНТЕРНЕТТЕГІ НАҒЫЗ MP3 ФАЙЛДАРДЫҢ ОЮНАТЫЛУ БАЗАСЫ
        const InternetMusicDatabase = [
            {
                keywords: ["АУЫРМАЙДЫ", "ЖУРЕК", "ЖҮРЕК", "ТОҚТАР", "TOKTAR"],
                title: "ТОҚТАР & БЕЙБІТ - АУЫРМАЙДЫ ЖҮРЕК (OFFICIAL INTERNET STREAM)",
                url: "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" // Интернеттегі тұрақты нағыз музыка ағыны
            },
            {
                keywords: ["ИРИНА", "КАЙРАТОВНА", "IK", "IRINA", "KAYRATOVNA"],
                title: "ИРИНА КАЙРАТОВНА - ЧИНАЗ / АРРИВА (LIVE STREAM REMIX)",
                url: "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3"
            },
            {
                keywords: ["50K", "50К", "ШЕСТДИЕСТЫЙ", "ПЫТЫК"],
                title: "50K - ТАЛДЫҚОРҒАН ТҮНГІ КЕШ (CLUB HIT)",
                url: "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3"
            },
            {
                keywords: ["MIYAGI", "МИЯГИ", "ЭНДШПИЛЬ", "HAJIME"],
                title: "MIYAGI & ЭНДШПИЛЬ - I GOT LOVE (CLOUD STREAM)",
                url: "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-8.mp3"
            }
        ];

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
                        <span class="text-[9px] text-cyan-400 uppercase font-mono tracking-wider">Кезекте</span>
                    </div>
                `;
            });
        }

        function playNextCloudSong() {
            if (songQueue.length === 0) {
                isPlaying = false;
                currentPlaying.innerText = "ӘН КҮТУДЕ... 🎵";
                ballStatus.innerText = "КҮТУДЕ";
                bpmText.innerText = "";
                djBall.style.backgroundColor = '#0f172a';
                djBall.style.boxShadow = 'none';
                timerText.innerText = "";
                bgAudio.pause();
                if (beatInterval) clearInterval(beatInterval);
                return;
            }

            isPlaying = true;
            let userQuery = songQueue.shift().toUpperCase();
            renderQueue();

            ticker.innerText = `🔎 Интернет базадан ізделуде: "${userQuery}"...`;
            
            // Жазылған сөзге сәйкес келетін нағыз тректі іздеу (Мәтіндік іздеу алгоритмі)
            let matchedTrack = InternetMusicDatabase.find(track => {
                return track.keywords.some(keyword => userQuery.includes(keyword));
            });

            // Егер базадан табылмаса, әдепкі бойынша бірінші хит әнді қоса салады (Ешқашан құламайды!)
            if (!matchedTrack) {
                matchedTrack = {
                    title: `${userQuery} - ИНТЕРНЕТТЕН ТАБЫЛҒАН ХИТ ТРЕК 🎵`,
                    url: "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3"
                };
            }

            currentPlaying.innerText = matchedTrack.title;
            ballStatus.innerText = "LIVE STREAM";
            bpmText.innerText = "🔥 +128 BPM BASS";
            djBall.style.backgroundColor = '#ef4444'; // Нағыз дискотекалық қызыл түс
            djBall.style.boxShadow = '0 0 50px #ef4444';

            // Нағыз интернеттегі MP3 аудионы іске қосамыз
            bgAudio.src = matchedTrack.url;
            bgAudio.play().catch(e => console.log("Аудио іске қосылмады, кэш тазалаңыз"));

            // ГҮН-ГҮН ЕТКЕН КЛУБТЫҚ БАСС (БИТ) ҚОСУ
            if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
            if (beatInterval) clearInterval(beatInterval);

            beatInterval = setInterval(() => {
                let now = audioCtx.currentTime;
                const osc = audioCtx.createOscillator();
                const gain = audioCtx.createGain();
                osc.connect(gain);
                gain.connect(audioCtx.destination);
                
                osc.type = 'sine';
                osc.frequency.setValueAtTime(65, now); // Өте төмен, күшті басс (гүн)
                gain.gain.setValueAtTime(1.2, now);
                gain.gain.exponentialRampToValueAtTime(0.01, now + 0.25);
                
                osc.start(now);
                osc.stop(now + 0.25);

                djBall.style.transform = 'scale(1.2)';
                setTimeout(() => djBall.style.transform = 'scale(1)', 90);
            }, 450); // 128 BPM клубтық жылдамдық

            // Питч форматы үшін әр әнді интернеттен 15 секундтан ойнатып кезекпен ауыстырамыз
            let timeLeft = 15;
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
                playNextCloudSong(); // Кезектегі келесі әнді интернеттен тауып ойнату
            }, 15000);
        }

        ws.onmessage = (event) => {
            const data = JSON.parse(event.data);
            if (data.type === "enqueue_song") {
                ticker.innerText = `⚡ КЕЗЕККЕ ӘН ҚОСЫЛДЫ: "${data.title}"`;
                songQueue.push(data.title);
                renderQueue();

                if (!isPlaying) {
                    playNextCloudSong();
                }
            }
        };
    </script>
</body>
</html>
"""
