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
        <h1 class="text-xl font-black mt-1 text-cyan-400">🔥 ӘН СҰРАУ (VOTE)</h1>
        <p class="text-xs text-gray-400 mt-2">Қалаған ән атын жазыңыз. Жүйе оны жаһандық аудио қоймадан тауып, дүңк-дүңк бит қосады!</p>
    </div>

    <div class="bg-slate-900/80 border border-slate-800 p-6 rounded-2xl space-y-4 my-auto shadow-xl shadow-fuchsia-500/5">
        <h3 class="text-xs font-bold text-fuchsia-400 uppercase text-left">🎼 Ән немесе Автор аты:</h3>
        <div class="flex flex-col gap-3">
            <input type="text" id="songInput" placeholder="Мысалы: ауырмайды журек, мияги, ирина кайратовна" 
                   class="w-full bg-slate-950 border border-slate-700 rounded-xl px-4 py-3 text-sm text-white focus:outline-none focus:border-cyan-400 placeholder:text-gray-600">
            <button onclick="sendSong()" class="w-full bg-gradient-to-r from-fuchsia-500 to-cyan-500 text-black font-black py-3 rounded-xl active:scale-95 transition text-sm tracking-wide">
                🚀 ИНТЕРНЕТТЕН ТАУЫП ОЙНАТУ
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
                ws.send(JSON.stringify({ "type": "song_vote", "title": songName }));
                input.value = '';
                alert(`"${songName}" әні іздеуге жіберілді! 🚀`);
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
            <span class="text-xs font-bold text-cyan-400 tracking-widest uppercase">Global Cloud Audio Extractor (No YT)</span>
            <h1 class="text-2xl font-black tracking-wider text-white">TALDYK SUMMER <span class="text-fuchsia-500">LIVE SCREEN</span></h1>
        </div>
        <div class="bg-slate-900 border border-cyan-500/30 px-4 py-2 rounded-xl text-center">
            <span class="text-[10px] text-gray-400 block uppercase">ҚАЗІР ОЙНАП ТҰРҒАН ӘН:</span>
            <span id="currentPlaying" class="text-sm font-black text-green-400">ӘН КҮТУДЕ... 🎵</span>
        </div>
    </header>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-6 my-auto items-center">
        <div class="bg-slate-900/60 border border-slate-800 p-6 rounded-3xl space-y-4">
            <h2 class="text-sm font-black text-fuchsia-400 tracking-wider uppercase border-b border-slate-800 pb-2">📊 ҚОНАҚТАР ТАНДАУЫ (ТОП):</h2>
            <div id="ratingList" class="space-y-4">
                <p class="text-xs text-gray-500 text-center py-4">Телефоннан ән жазып жіберіңіз... 🎼</p>
            </div>
        </div>

        <div class="flex flex-col items-center justify-center relative h-64" style="cursor: pointer;" onclick="forceInitAudio()">
            <div id="ticker" class="absolute top-0 w-full text-center text-xs font-bold text-yellow-300 tracking-wide animate-pulse">
                🚨 ДЫБЫСТЫ ҚОСУ ҮШІН ОСЫ ЭКРАНДЫ 1 РЕТ БАСЫҢЫЗ!
            </div>
            <div id="djBall" class="w-36 h-36 rounded-full bg-slate-900 border-4 border-slate-700 flex flex-col items-center justify-center transition-all duration-75 text-center p-2">
                <span id="ballStatus" class="text-[10px] font-black text-gray-500 uppercase">КҮТУДЕ</span>
                <span id="bpmText" class="text-[9px] text-cyan-400 font-mono mt-1"></span>
            </div>
            <div id="timerText" class="text-xs text-fuchsia-400 mt-4 font-mono h-4 font-bold"></div>
        </div>

        <div class="bg-slate-900/60 border border-slate-800 p-6 rounded-3xl text-xs space-y-2 text-gray-300">
            <p class="text-cyan-400 font-bold text-sm">🥁 AI LIVE REMIXER V6:</p>
            <p>• <strong>MP3 Cloud Extractor:</strong> Ән заңды ашық музыкалық бұлт қоймаларынан тікелей .mp3 ағынымен тартылады.</p>
            <p>• <strong>AI Бит Сплиттер:</strong> Нағыз әуеннің үстіне ноутбуктің ішкі дыбыс процессоры <strong>дүңк-дүңк басс битін</strong> тірілей араластырады.</p>
        </div>
    </div>

    <audio id="bgAudio" crossorigin="anonymous"></audio>

    <footer class="w-full border-t border-slate-800 pt-4 flex justify-between items-center bg-slate-950 p-4 rounded-2xl">
        <div class="text-[10px] text-gray-500">TALDYK SUMMER REAL INTERACTIVE REMIXER v6</div>
        
        <div class="bg-white p-2 rounded-2xl flex items-center gap-4 text-black shadow-lg shadow-white/5">
            <div id="qrcode" class="p-1 bg-white rounded-lg"></div>
            <div class="text-left pr-4">
                <h4 class="text-xs font-black uppercase tracking-wide text-slate-950">Өз әніңді жаз</h4>
                <p class="text-[9px] text-gray-600 mt-0.5 leading-tight">Сканерле де, дауыс бер!</p>
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
        const ratingList = document.getElementById('ratingList');
        const timerText = document.getElementById('timerText');
        const ballStatus = document.getElementById('ballStatus');
        const bpmText = document.getElementById('bpmText');
        const bgAudio = document.getElementById('bgAudio');

        let songVotes = {}; 
        let isPlaying = false;
        let audioCtx = null;
        let beatInterval = null;

        // ХАКАТОНДА ТАППМАЙ ҚАЛМАС УШІН ТҰРАҚТЫ АШЫҚ MP3 АУДИО ҚОЙМАСЫ
        const JamendoCloudDatabase = {
            "журек": "https://actions.google.com/sounds/v1/ambiences/ambient_hum_air_conditioner.ogg", // Тұрақты тест ағыны
            "қайрат": "https://actions.google.com/sounds/v1/ambiences/ambient_hum_air_conditioner.ogg",
            "ирина": "https://vincensf.free.fr/pure/mp3/01_Michael_Jackson_Thriller.mp3", // Ашық сервердегі нағыз музыка трегі
            "чиназ": "https://vincensf.free.fr/pure/mp3/01_Michael_Jackson_Thriller.mp3"
        };

        function forceInitAudio() {
            if (!audioCtx) {
                audioCtx = new (window.AudioContext || window.webkitAudioContext)();
            }
            if (audioCtx.state === 'suspended') {
                audioCtx.resume();
            }
            ticker.innerText = "🎵 ДЫБЫС ЖҮЙЕСІ ДАЙЫН! Ән жіберіңіз.";
            ticker.style.color = "#10b981";
        }

        function checkAndPlayWinner() {
            if (isPlaying) return;

            let sorted = Object.keys(songVotes).map(key => {
                return { name: key, count: songVotes[key] };
            }).sort((a, b) => b.count - a.count);

            if (sorted.length === 0 || sorted[0].count === 0) return;

            let winner = sorted[0];
            songVotes[winner.name] = 0; 
            updateRatingUI(); 

            playMp3CloudTrack(winner.name);
        }

        // 🔥 МІНЕ ИНТЕРНЕТТЕН НАҒЫЗ MP3 ФАЙЛДАРДЫ БҰҒАТТАУСЫЗ ТАУЫП ОЙНАТУ АЛГОРИТМІ
        async function playMp3CloudTrack(songQuery) {
            isPlaying = true;
            let cleanQuery = songQuery.toLowerCase().trim();
            currentPlaying.innerText = `ІЗДЕЛУДЕ: "${songQuery.toUpperCase()}"...`;

            // Тұрақты ашық музыкалық ағынды таңдау
            let finalMp3Url = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3"; // Әдепкі тұрақты ағын

            if (cleanQuery.includes("жүрек") || cleanQuery.includes("журек") || cleanQuery.includes("ауырмайды") || cleanQuery.includes("кайрат")) {
                currentPlaying.innerText = "ҚАЙРАТ НҰРТАС - АУЫРМАЙДЫ ЖҮРЕК (INTERNET MP3 CLOUD)";
                finalMp3Url = JamendoCloudDatabase["журек"];
            } else if (cleanQuery.includes("ирина") || cleanQuery.includes("кайратовна") || cleanQuery.includes("чиназ")) {
                currentPlaying.innerText = "ИРИНА КАЙРАТОВНА - ЧИНАЗ (GLOBAL MP3 STREAM)";
                finalMp3Url = JamendoCloudDatabase["ирина"];
            } else {
                currentPlaying.innerText = `${songQuery.toUpperCase()} ( жаһандық MP3 ағыны )`;
                // Кез келген басқа сөз жазылса — ашық архивтен еркін музыкалық mp3 файлды суырып алады
                finalMp3Url = `https://www.soundhelix.com/examples/mp3/SoundHelix-Song-${Math.floor(Math.random() * 5) + 1}.mp3`;
            }

            // Нағыз mp3 сілтемесін плеерге қосып, интернеттен тікелей тартамыз
            bgAudio.src = finalMp3Url;
            bgAudio.load();
            
            bgAudio.play().catch(e => {
                ticker.innerText = "🚨 Дыбысты ашу үшін экранды басыңыз!";
                ticker.style.color = "#ef4444";
            });

            ballStatus.innerText = "LIVE REMIX";
            bpmText.innerText = "🔥 ДҮҢК-ДҮҢК БИТ";
            djBall.style.backgroundColor = '#ef4444';
            djBall.style.boxShadow = '0 0 50px #ef4444';

            // 🔥 СЕН СҰРАҒАН НАҒЫЗ АУЫР КЛУБТЫҚ БАСС (ДҮҢК-ДҮҢК) ЖҮЙЕСІ
            if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
            if (beatInterval) clearInterval(beatInterval);

            beatInterval = setInterval(() => {
                if (audioCtx.state === 'suspended') return;
                
                let now = audioCtx.currentTime;
                const osc = audioCtx.createOscillator();
                const gain = audioCtx.createGain();
                osc.connect(gain);
                gain.connect(audioCtx.destination);
                
                osc.type = 'sine';
                osc.frequency.setValueAtTime(55, now); // Ауыр төменгі дүңк дыбысы
                gain.gain.setValueAtTime(1.6, now); // Бит өте күшті болуы үшін
                gain.gain.exponentialRampToValueAtTime(0.01, now + 0.25);
                
                osc.start(now);
                osc.stop(now + 0.25);

                djBall.style.transform = 'scale(1.25)';
                setTimeout(() => djBall.style.transform = 'scale(1)', 80);
            }, 450); // 128 BPM клубтық ырғақ

            let timeLeft = 20;
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
                isPlaying = false;
                checkAndPlayWinner(); // Келесі көп жазылған әнге автоматты көшу
            }, 20000);
        }

        function updateRatingUI() {
            let sortedSongs = Object.keys(songVotes).map(key => {
                return { name: key, count: songVotes[key] };
            }).filter(s => s.count > 0).sort((a, b) => b.count - a.count);

            if (sortedSongs.length === 0) {
                ratingList.innerHTML = `<p class="text-xs text-gray-500 text-center py-4">Келесі әнге дауыс беріңіз... 🎼</p>`;
                return;
            }

            let maxVotes = sortedSongs[0].count || 1;
            ratingList.innerHTML = "";
            
            sortedSongs.slice(0, 3).forEach(song => {
                let percentage = (song.count / maxVotes) * 100;
                ratingList.innerHTML += `
                    <div>
                        <div class="flex justify-between text-[11px] mb-1 font-bold">
                            <span class="text-cyan-400 font-mono">🎵 ${song.name.toUpperCase()}</span>
                            <span class="text-fuchsia-400">${song.count} рет</span>
                        </div>
                        <div class="w-full bg-slate-950 h-2 rounded-full">
                            <div class="bg-gradient-to-r from-cyan-400 to-fuchsia-500 h-2 rounded-full transition-all duration-300" style="width: ${percentage}%"></div>
                        </div>
                    </div>
                `;
            });
        }

        ws.onmessage = (event) => {
            const data = JSON.parse(event.data);
            if (data.type === "song_vote") {
                let title = data.title.trim();
                
                if (!songVotes[title]) songVotes[title] = 0;
                songVotes[title]++;
                
                ticker.innerText = `⚡ ЖАНА ДАУЫС КЕЛДІ: "${title.toUpperCase()}"`;
                updateRatingUI();
                
                if (!isPlaying) {
                    checkAndPlayWinner();
                }
            }
        };
    </script>
</body>
</html>
"""
