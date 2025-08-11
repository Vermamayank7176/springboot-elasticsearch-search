import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;
import lombok.RequiredArgsConstructor;
import org.springframework.boot.CommandLineRunner;
import org.springframework.stereotype.Component;

import java.io.InputStream;
import java.util.List;

@Component
@RequiredArgsConstructor
public class DataLoader implements CommandLineRunner {

    private final CourseRepo courseRepo;
    private final ObjectMapper objectMapper;

    @Override
    public void run(String... args) throws Exception {
        if (courseRepo.count() == 0) {
            InputStream inputStream = getClass().getResourceAsStream("/sample-courses.json");
            List<CourseDocument> courses = objectMapper.readValue(inputStream,
                    new TypeReference<List<CourseDocument>>() {});
            courseRepo.saveAll(courses);
            System.out.println("Loaded " + courses.size() + " courses into Elasticsearch");
        }
    }
}
