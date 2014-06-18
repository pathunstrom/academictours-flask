Jan = 0
Feb = 1
Mar = 2
Apr = 3
May = 4
Jun = 5
Jul = 6
Aug = 7
Sep = 8
Oct = 9
Nov = 10
Dec = 11

sample_copy = """
              <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.
              Curabitur arcu tellus, condimentum at mauris porta, sodales
              placerat orci. Aenean lacinia aliquam ultricies. In ultricies
              bibendum nisl a rhoncus. Morbi tempus eros eu urna tincidunt
              dapibus. Nam tempor, nisl at sodales adipiscing, elit arcu
              vehicula arcu, et vulputate nunc lorem quis dolor. Ut porta
              auctor ultricies. Ut nec ante porttitor, aliquam est ut,
              placerat turpis. Sed posuere orci id dui varius, id rhoncus
              felis varius. Nam suscipit lorem eget ligula vulputate, sed
              interdum odio sagittis.</p>
              <p>Cras id magna vitae velit placerat scelerisque id id diam.
              Sed hendrerit faucibus nisl eu lobortis. Praesent accumsan
              pellentesque nunc a pellentesque. In hac habitasse platea
              dictumst. Morbi et viverra enim. Donec tempus orci et ipsum
              mattis, vitae posuere urna tempus. Nam iaculis rhoncus augue, in
              tincidunt nisl mattis vitae. Suspendisse pretium urna nec
              tristique mattis. Mauris mollis nisi at sem sodales, at tincidunt
              libero aliquet. Nullam vitae feugiat nibh.</p>
              """

tours = [{"destination": "Malta", "name": "Malta-Sicily Delight",
          "banner_image": "MaltaBayWithArmor.jpg",
          "thumbnail": "logo.png",
          "copy": sample_copy,
          "summary": "Our star tour.\
          Visit Malta and Sicily with our hand crafted tours.",
          "featured": True},
         ]

days = [{"tour": "Malta-Sicily Delight", "day": 1,
         "summary": "Short summary of day."},
        {"tour": "Malta-Sicily Delight", "day": 2,
         "summary": "Short summary of day."}]

landmark_relations = [{"tour": "Malta-Sicily Delight", "day": 1,
                       "landmark": "Sample Landmark"},
                      {"tour": "Malta-Sicily Delight", "day": 1,
                       "landmark": "Another Sample Landmark"}]

prices = [{"tour": "Malta-Sicily Delight", "month": Jun, "price": "999"},
         {"tour": "Malta-Sicily Delight", "month": Jul, "price": "1099"},
         {"tour": "Malta-Sicily Delight", "month": Aug, "price": "1199"}]