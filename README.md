<h1 align='center'>Data-Encryptor</h1>

<p>This is a programm to encrypt files and folders. The final result is a folder with binary-encrypted pickle files.</p>

<p>The programm has two versions cli and api, the api-version is in development and the cli is ready to use</p>

<p>In this first version it only accepts .mp4 files to be encrypt.</p>

<h2>Encrypter_CLI</h2>

<h3>To run it</h3>
<pre>
#standing on Data-Encryptor folder
pip install -r requirements.txt
python cli/encrypter_cli.py
</pre>

<h3>Path and password</h3>
<img src="img/Screenshot from 2024-01-30 10-45-00.png">

<h3>Results</h3>
<p>After encrypt you will end up with a password.pickle file needed to decrypt it and a new folder called /encrypted_files with the new files in pickle format.</p>
<img src="img/Screenshot from 2024-01-30 10-47-26.png">

<h2>Decrypter_CLI</h2>
<p>To decrypt the file password.pickle must be in the same folder as the rest of pickle files.</p>