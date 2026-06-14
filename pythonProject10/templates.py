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
        <h1 class="text-xl font-black mt-1 text-cyan-400">🔥 КЕЗ КЕЛГЕН ӘНДІ ЖАЗУ</h1>
        <p class="text-xs text-gray-400 mt-2">Ойыңызға келген кез келген ән атын немесе авторын жазыңыз. Жүйе оны интернеттен тауып, дүңк-дүңк бит қосады!</p>
    </div>

    <div class="bg-slate-900/80 border border-slate-800 p-6 rounded-2xl space-y-4 my-auto shadow-xl shadow-fuchsia-500/5">
        <h3 class="text-xs font-bold text-fuchsia-400 uppercase text-left">🎼 Ән немесе Автор аты:</h3>
        <div class="flex flex-col gap-3">
            <input type="text" id="songInput" placeholder="Мысалы: Мияги, Каират Нуртас, 50k, Ирина Кайратовна" 
                   class="w-full bg-slate-950 border border-slate-700 rounded-xl px-4 py-3 text-sm text-white focus:outline-none focus:border-cyan-400 placeholder:text-gray-600">
            <button onclick="sendSong()" class="w-full bg-gradient-to-r from-cyan-500 to-fuchsia-500 text-black font-black py-3 rounded-xl active:scale-95 transition text-sm tracking-wide">
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
                alert(`"${songName}" әні плейлист кезегіне қосылды! 🚀`);
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
            <span class="text-xs font-bold text-cyan-400 tracking-widest uppercase">Global Live Music Extractor</span>
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
                🚨 ДЫБЫСТЫ ҚОСУ ҮШІН ЭКРАНДЫ 1 РЕТ БАСЫҢЫЗ!
            </div>
            
            <div class="w-full h-40 bg-black rounded-xl overflow-hidden border border-slate-800 shadow-lg relative">
                <div id="videoContainer" class="w-full h-full">
                    <p class="text-[10px] text-center text-gray-500 pt-16">Музыка күтілуде...</p>
                </div>
            </div>

            <div id="djBall" class="w-14 h-14 rounded-full bg-cyan-500 border-2 border-white flex items-center justify-center transition-all duration-75 text-center mt-2">
                <span id="bpmText" class="text-[8px] text-black font-mono font-bold">BPM</span>
            </div>
            <div id="timerText" class="text-xs text-fuchsia-400 mt-2 font-mono h-4 font-bold"></div>
        </div>

        <div class="bg-slate-900/60 border border-slate-800 p-6 rounded-3xl text-xs space-y-2 text-gray-300">
            <p class="text-cyan-400 font-bold text-sm">🥁 AI LIVE REMIXER V6:</p>
            <p>• <strong>Global Search Engine:</strong> Адамдар не жазса да, жүйе оны ашық интернет қоймасынан тауып, тікелей ойнатады.</p>
            <p>• <strong>Дүңк-Дүңк Бит:</strong> Ноутбуктің ішкі аудио картасы табылған әннің үстіне <strong>ауыр фестивальдік басс</strong> қосады.</p>
        </div>
    </div>

    <footer class="w-full border-t border-slate-800 pt-4 flex justify-between items-center bg-slate-950 p-4 rounded-2xl">
        <div class="text-[10px] text-gray-500">TALDYK SUMMER REAL INTERACTIVE REMIXER v6</div>
        
        <div class="bg-white p-2 rounded-2xl flex items-center gap-4 text-black shadow-lg shadow-white/5">
            <div id="qrcode" class="p-1 bg-white rounded-lg"></div>
            <div class="text-left pr-4">
                <h4 class="text-xs font-black uppercase tracking-wide text-slate-950">Өз әніңді жаз</h4>
                <p class="text-[9px] text-gray-600 mt-0.5 leading-tight">Камерамен сканерле де, дауыс бер!</p>
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
        const bpmText = document.getElementById('bpmText');
        const videoContainer = document.getElementById('videoContainer');

        let songVotes = {}; 
        let isPlaying = false;
        let audioCtx = null;
        let beatInterval = null;

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

            playLiveInternetTrack(winner.name);
        }

        // 🔥 МІНЕ ЕҢ БАСТЫ МАГИЯ: КЕЗ КЕЛГЕН ӘНДІ ИНТЕРНЕТТЕН (DUCKDUCKGO REALTIME SCRAPER) АРҚЫЛЫ ІЗДЕП ТАБУ
        async function playLiveInternetTrack(songQuery) {
            isPlaying = true;
            currentPlaying.innerText = `ІЗДЕЛУДЕ: "${songQuery.toUpperCase()}"...`;
            ticker.innerText = `🔎 Интернеттен нағыз видео ізделуде...`;

            try {
                // Ашық іздеу проксиі арқылы YouTube-тен бірінші шыққан нағыз видеоның ID-ін тауып аламыз
                let searchUrl = `https://api.allorigins.win/get?url=${encodeURIComponent('https://html.duckduckgo.com/html/?q=site:youtube.com/watch ' + songQuery)}`;
                let response = await fetch(searchUrl);
                let resData = await response.json();
                
                // Мәтіннің ішінен /watch?v= ИД-ін суырып алу алгоритмі
                let htmlContent = resData.contents;
                let match = htmlContent.match(/v=([a-zA-Z0-9_-]{11})/);
                
                let videoId = "93_bMAnfV58"; // Егер ештеңе таппаса, әдепкі бойынша Қайрат Нұртастың ресми клипін қояды
                if (match && match[1]) {
                    videoId = match[1];
                }

                currentPlaying.innerText = `${songQuery.toUpperCase()} (YOUTUBE LIVE INTERNET)`;
                ballStatus.innerText = "LIVE REMIX";
                bpmText.innerText = "🥁 БИТ";
                djBall.style.backgroundColor = '#ef4444';
                djBall.style.boxShadow = '0 0 50px #ef4444';

                // Нағыз табылған видеоны экранға шығарамыз (Бұғатталмайтын ресми халықаралық ойнатқыш)
                videoContainer.innerHTML = `<iframe class="w-full h-full" src="https://www.youtube.com/embed/${videoId}?autoplay=1&mute=0&rel=0" frameborder="0" allow="autoplay; encrypted-media"></iframe>`;

                // 🔥 ДҮҢК-ДҮҢК КЛУБТЫҚ БАСС (БИТ) ҚОСУ
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
                    osc.frequency.setValueAtTime(55, now); 
                    gain.gain.setValueAtTime(1.5, now);
                    gain.gain.exponentialRampToValueAtTime(0.01, now + 0.25);
                    
                    osc.start(now);
                    osc.stop(now + 0.25);

                    djBall.style.transform = 'scale(1.3)';
                    setTimeout(() => djBall.style.transform = 'scale(1)', 80);
                }, 450); // 128 BPM клубтық жылдамдық

                // Әр ән сахнада 25 секунд ойнайды
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
                    videoContainer.innerHTML = `<p class="text-[10px] text-center text-gray-500 pt-16">Келесі ән жүктелуде...</p>`;
                    if (beatInterval) clearInterval(beatInterval);
                    isPlaying = false;
                    checkAndPlayWinner(); 
                }, 25000);

            } catch (error) {
                console.log(error);
                ticker.innerText = "🚨 Интернет байланысы нашар, қайта ізделуде...";
                isPlaying = false;
                setTimeout(() => { playLiveInternetTrack(songQuery); }, 2000);
            }
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
