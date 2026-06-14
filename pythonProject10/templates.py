# templates.py

HTML_CONTROLLER = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Taldyk Summer - Ән Таңдау</title>
    <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
</head>
<body class="h-screen bg-slate-950 text-white flex flex-col justify-between p-6 text-center select-none overflow-hidden">
    
    <div>
        <span class="text-xs font-bold text-fuchsia-500 uppercase tracking-widest">Taldyk Summer • Live DJ</span>
        <h1 class="text-xl font-black mt-1 text-cyan-400">ПЛЕЙЛИСТКЕ ӘН ҚОСУ 🎵</h1>
        <p class="text-xs text-gray-400 mt-2">Қалаған әніңіздің атын дәл жазып жіберіңіз. Көп сұралған ән автоматты түрде ойнайды!</p>
    </div>

    <div class="bg-slate-900/80 border border-slate-800 p-6 rounded-2xl space-y-4 my-auto shadow-xl shadow-fuchsia-500/5">
        <h3 class="text-xs font-bold text-fuchsia-400 uppercase text-left">🎼 Ән немесе Автор аты:</h3>
        <div class="flex flex-col gap-3">
            <input type="text" id="songInput" placeholder="Мысалы: Ирина Кайратовна, 50k немесе Ганвест" 
                   class="w-full bg-slate-950 border border-slate-700 rounded-xl px-4 py-3 text-sm text-white focus:outline-none focus:border-cyan-400 placeholder:text-gray-600">
            <button onclick="sendSong()" class="w-full bg-gradient-to-r from-cyan-500 to-blue-600 text-black font-black py-3 rounded-xl active:scale-95 transition text-sm tracking-wide">
                🔥 ӘНГЕ ДАУЫС БЕРУ
            </button>
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

        function sendSong() {
            const input = document.getElementById('songInput');
            const songName = input.value.trim();
            if (songName && ws.readyState === WebSocket.OPEN) {
                // Серверге хабарлама түрінде ән атын жібереміз
                ws.send(JSON.stringify({ "type": "song_vote", "title": songName.toUpperCase() }));
                input.value = '';
                alert(`"${songName}" плейлистке қосылды және дауыс берілді! 🚀`);
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
            <span class="text-xs font-bold text-cyan-400 uppercase tracking-widest">Crowdsourced DJ Engine</span>
            <h1 class="text-2xl font-black tracking-wider text-white">TALDYK SUMMER <span class="text-fuchsia-500">LIVE SCREEN</span></h1>
        </div>
        <div class="bg-slate-900 border border-cyan-500/30 px-4 py-2 rounded-xl text-center">
            <span class="text-[10px] text-gray-400 block uppercase">ҚАЗІР ОЙНАП ТҰРҒАН ӘН:</span>
            <span id="currentPlaying" class="text-sm font-black text-green-400">ӘН КҮТУДЕ... 🎵</span>
        </div>
    </header>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-6 my-auto items-center">
        <div class="bg-slate-900/60 border border-slate-800 p-6 rounded-3xl space-y-4">
            <h2 class="text-sm font-black text-fuchsia-400 tracking-wider uppercase border-b border-slate-800 pb-2">📊 ЕҢ КӨП СҰРАЛҒАН ТРЕКТЕР:</h2>
            <div id="ratingList" class="space-y-4">
                <p class="text-xs text-gray-500 text-center py-4">Қонақтардан ән күтілуде... 🎼</p>
            </div>
        </div>

        <div class="flex flex-col items-center justify-center relative h-64">
            <div id="ticker" class="absolute top-0 w-full text-center text-md font-bold text-yellow-300 tracking-wide animate-pulse">
                Салқын кешке өз әніңізді қосыңыз! ✨
            </div>
            <div id="djBall" class="w-32 h-32 rounded-full bg-cyan-500 border-4 border-white neon-shadow flex items-center justify-center transition-all duration-300">
                <span class="text-xs font-black text-black text-center">LIVE<br>BEAT</span>
            </div>
        </div>

        <div class="bg-slate-900/60 border border-slate-800 p-6 rounded-3xl text-xs space-y-2 text-gray-300">
            <p class="text-cyan-400 font-bold text-sm">🧠 ДАТА-АНАЛИТИКА ЖҮЙЕСІ:</p>
            <p>• Жүйе келген мәтіндерді нақты уақытта (Real-time) талдайды.</p>
            <p>• Бірдей жазылған әндерді автоматты түрде топтап, рейтинг түзеді.</p>
            <p class="text-fuchsia-400 font-medium mt-2">Бұл — диджейсіз-ақ халықтың қалауымен жұмыс істейтін толыққанды Автономды Смарт-Плейлист!</p>
        </div>
    </div>

    <footer class="w-full border-t border-slate-800 pt-4 flex justify-between items-center bg-slate-950 p-4 rounded-2xl">
        <div class="text-[10px] text-gray-500">TALDYK SUMMER SMART PLAYLIST ENGINE v3</div>
        <div class="bg-white p-1 rounded-xl flex items-center gap-2">
            <img id="qrImg" src="" alt="QR" class="w-14 h-14">
            <div class="text-black text-left pr-2">
                <h4 class="text-[10px] font-black uppercase">Өз әніңді жаз</h4>
                <p class="text-[8px] text-gray-500 mt-0.5">Сканерле де, атын жібер!</p>
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
        const ratingList = document.getElementById('ratingList');

        // Әндер мен олардың дауыстарын сақтайтын динамикалық объект
        let songVotes = {};
        let audioCtx = null;
        let currentInterval = null;
        let lastWinner = "";

        // Ән ауысқанда ноутбуктен динамикалық түрде әртүрлі бит шығару
        function triggerAudioBeat(songTitle) {
            if (songTitle === lastWinner) return; // Егер ән ауыспаса, битті бұзбаймыз
            lastWinner = songTitle;

            if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
            if (currentInterval) clearInterval(currentInterval);

            // Әннің атындағы әріптердің санына қарай дыбыс жиілігін (Тон) өзгерту (Магия!)
            let hashFreq = 70 + (songTitle.length * 5); 
            let speed = 400;

            currentPlaying.innerText = songTitle;
            djBall.style.backgroundColor = '#ec4899';

            currentInterval = setInterval(() => {
                const osc = audioCtx.createOscillator();
                const gain = audioCtx.createGain();
                osc.connect(gain);
                gain.connect(audioCtx.destination);
                
                osc.type = 'sine';
                osc.frequency.setValueAtTime(hashFreq, audioCtx.currentTime);
                gain.gain.setValueAtTime(0.7, audioCtx.currentTime);
                gain.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.25);
                
                osc.start();
                osc.stop(audioCtx.currentTime + 0.25);

                djBall.style.transform = 'scale(1.25)';
                djBall.style.boxShadow = '0 0 60px #ec4899';
                setTimeout(() => {
                    djBall.style.transform = 'scale(1)';
                    djBall.style.boxShadow = '0 0 40px #00f0ff';
                }, 120);
            }, speed);
        }

        // Келген мәтіндерді сұрыптап, ТОП-3 экранға шығару
        function processSongVote(title) {
            // Егер бұл ән бұрын жазылмаса, тізімге 0 дауыспен қосамыз
            if (!songVotes[title]) {
                songVotes[title] = 0;
            }
            songVotes[title]++; // Дауысты 1-ге өсіреміз

            // Объектіні массивке айналдырып, дауыс саны бойынша сұрыптаймыз (Сортировка)
            let sortedSongs = Object.keys(songVotes).map(key => {
                return { name: key, count: songVotes[key] };
            }).sort((a, b) => b.count - a.count);

            // Ең көп дауыс жинаған ТОП-3 әнді ғана алу
            let topSongs = sortedSongs.slice(0, 3);
            let maxVotes = topSongs[0].count;

            // Экрандағы HTML-ді тірілей жаңарту
            ratingList.innerHTML = "";
            topSongs.forEach(song => {
                let percentage = (song.count / maxVotes) * 100;
                ratingList.innerHTML += `
                    <div>
                        <div class="flex justify-between text-xs mb-1 font-bold">
                            <span class="text-cyan-400">🎵 ${song.name}</span>
                            <span class="text-fuchsia-400">${song.count} рет сұралды</span>
                        </div>
                        <div class="w-full bg-slate-950 h-2 rounded-full">
                            <div class="bg-gradient-to-r from-cyan-400 to-fuchsia-500 h-2 rounded-full transition-all duration-500" style="width: ${percentage}%"></div>
                        </div>
                    </div>
                `;
            });

            // Бірінші орында тұрған әнді ойнатуға жібереміз
            if (topSongs.length > 0) {
                triggerAudioBeat(topSongs[0].name);
            }
        }

        ws.onmessage = (event) => {
            const data = JSON.parse(event.data);

            if (data.type === "song_vote") {
                ticker.innerText = `⚡ ЖАҢА ТРЕК ЖАЗЫЛДЫ: "${data.title}"`;
                processSongVote(data.title);
            }
        };
    </script>
</body>
</html>
"""
