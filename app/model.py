import tour


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

copy = [{"name": "about",
         "value": "Founded in 1984, Academic Tours and Travel is a leading \
                  specialist in travel to Malta and Sicily. They also are \
                  home to experts in many European destinations including \
                  Italy and Romania."},
        {"name": "pledge",
         "value": '<p><em>"From Concept to Completion"</em></p> \
                  <p>Our agents will work with you from the first idea until \
                  you pick you unpack. If we ever receive complaints about a \
                  local provider they are investigated and blacklisted for at \
                  least one year.</p>'},
        {"name": "selected tours",
         "value": "<p>Our travel experts have designed tours ready to book to \
                  some of the greatest destinations in the Mediterraenean and \
                  Southern Asia.</p> \
                  <p>take up room so we can see what things look like. This is \
                  important, of course.</p>"},
        {"name": "custom tours",
         "value": "<p>Have an idea for a dream vacation? Let us help.</p> \
                  <p>Set aside your worries and let our experts guide you in \
                  making memories. They have decades of experience planning \
                  perfect trips with first hand knowledge of Europe and Asia. \
                  </p>"}
        ]

regions = [{"name": "Mediterranean",
            "summary": "This is a summary for the Mediterranean.",
            "copy": sample_copy,
            "thumbnail": "logo.png"},
           {"name": "Asia",
            "summary": "This is a summary for Asia.",
            "copy": sample_copy,
            "thumbnail": "logo.png"}]

destinations = [{"name": "Malta", "region": "Mediterranean",
                 "summary": "The jewel of the Mediterranean",
                 "copy": sample_copy, "featured": True,
                 "thumbnail": "logo.png",
                 "banner_image": "MaltaBayWithArmor.jpg"},
                {"name": "Sicily", "region": "Mediterranean",
                 "summary": "Sicily short summary.",
                 "copy": sample_copy, "featured": False,
                 "thumbnail": "logo.png",
                 "banner_image": "MaltaBayWithArmor.jpg"},
                {"name": "Italy", "region": "Mediterranean",
                 "summary": "Italy short summary.",
                 "copy": sample_copy, "featured": False,
                 "thumbnail": "logo.png",
                 "banner_image": "MaltaBayWithArmor.jpg"},
                {"name": "Sardinia", "region": "Mediterranean",
                 "summary": "Sardinia short summary.",
                 "copy": sample_copy, "featured": False,
                 "thumbnail": "logo.png",
                 "banner_image": "MaltaBayWithArmor.jpg"},
                {"name": "Tunisia", "region": "Mediterranean",
                 "summary": "Tunisia short summary.",
                 "copy": sample_copy, "featured": False,
                 "thumbnail": "logo.png",
                 "banner_image": "MaltaBayWithArmor.jpg"},
                {"name": "Bhutan", "region": "Asia",
                 "summary": "Bhutan short summary.",
                 "copy": sample_copy, "featured": False,
                 "thumbnail": "logo.png",
                 "banner_image": "MaltaBayWithArmor.jpg"},
                {"name": "Nepal", "region": "Asia",
                 "summary": "Nepal short summary.",
                 "copy": sample_copy, "featured": False,
                 "thumbnail": "logo.png",
                 "banner_image": "MaltaBayWithArmor.jpg"},
                ]

landmarks = [{"name": "Sample Landmark", "summary": "Sample summary."},
             {"name": "Another Sample Landmark",
              "summary": "Another sample summary."}]

month = ["January", "March", "April", "May", "June", "July",
         "August", "September", "October", "November", "December"]

tours = tour.tours
days = tour.days
day_landmark = tour.landmark_relations
prices = tour.prices