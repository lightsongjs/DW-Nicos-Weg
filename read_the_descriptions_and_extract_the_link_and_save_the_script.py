import os,glob
import requests
from bs4 import BeautifulSoup


#PAS1 - extract the description from every youtubevideo - the description contains the url to the script
# youtube-dl https://www.youtube.com/watch?v=4o0r9unT4L4 --write-description --skip-download --youtube-skip-dash-manifest

os.chdir('materiale')
lista_materiale = os.listdir()
os.chdir('..')



# for file in glob.glob("*.description"):
#     with open(file) as f:
#     	first_line = f.readline()
#     	word_list = first_line.split()
#     	# print(word_list)
#     	# url = word_list[-1]+"/lm"
#     	url = word_list[-1].split('/')[-1]
#     	lista_url.append(url)
#     	# print(url.split('/'))
lessonNr=0	

for file in lista_materiale:
	#Crearea titlului lectiilor
	split_lesson_nr = file.split('-')
	episode_level=file.split('-')[0].strip()
	episode_nr=file.split('-')[2].strip()
	episode_title=file.split('-')[3].strip()



	os.chdir('materiale')
	with open(file) as f:
		first_line = f.readline()
		word_list = first_line.split()
		# print(word_list)
		# url = word_list[-1]+"/lm"
		url = word_list[-1].split('/')[-1]
		os.chdir('..')
		

		try:
			URL='https://learngerman.dw.com/en/'+ url + '/lm'
			page = requests.get(URL)
			
			soup = BeautifulSoup(page.content, 'html.parser')
			title = soup.find('h1').text		

			results = soup.find('div', class_='row vocabulary').text
			# print(results.text)

			lessonNr=lessonNr+1

			# filename=str(lessonNr) + '.' +title+'.txt'
			filenameWithExtension= f'{episode_level}-{episode_nr}-{episode_title}.txt'
			filename= f'{episode_level}-{episode_nr}-{episode_title}'

			
			if '?' in filename:
				filename= filename.replace("?", "")

				# Scrie in acelasi fisier
			# with open(filename, "w", encoding="utf-8") as f:
			# 		f.write('')
			# 		f.write(title +'')
			# 		f.write(results+'')
			# 		f.write('==============================================='+ '\n')

			with open(f'script4.txt', "a", encoding="utf-8") as f:
				f.write('')
				f.write(filename)
				f.write(results+'')
				f.write('==============================================='+ '\n')
				

			with open(filenameWithExtension, "w", encoding="utf-8") as f:
				f.write('')
				f.write(filename)
				f.write(results+'')
				f.write('==============================================='+ '\n')

					
			

		except:
			print(f'Eroare la fisierul {file}')






    	
    	







# for f in lista_url:
# 	try:
# 		URL='https://learngerman.dw.com/en/'+ f + '/lm'
# 		page = requests.get(URL)

# 		soup = BeautifulSoup(page.content, 'html.parser')
# 		title = soup.find('h1').text		

# 		results = soup.find('div', class_='row vocabulary').text
# 		# print(results.text)

# 		os.chdir('test')
	
# 		lessonNr=lessonNr+1
# 		# Scrie in fisiere separate

# 		filename=lessonNr + '.' +title+'.txt'

# 		with open(filename, "w", encoding="utf-8") as f:
# 			f.write('')
# 			f.write(title +'')
# 			f.write(results+'')
# 			f.write('==============================================='+ '\n')

# 		# Scrie in acelasi fisier
# 		with open(f'script.txt', "a", encoding="utf-8") as f:
# 			f.write('')
# 			f.write(title +'')
# 			f.write(results+'')
# 			f.write('==============================================='+ '\n')

			
# 		os.chdir('..')

# 	except:
# 		print(f'Eroare la fisierul {f}')