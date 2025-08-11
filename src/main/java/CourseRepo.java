import org.springframework.data.elasticsearch.repository.ElasticsearchRepository;

public interface CourseRepo extends ElasticsearchRepository<CourseDocument, String> {

}
